/*
 *
 */

#include "CoverHubDominance.h"
#include "../auxiliary/SignalHandling.h"
#include "../auxiliary/Parallel.h"
#include <atomic>

void NetworKit::CoverHubDominance::run() {
	hasRun = false;
	Aux::SignalHandler handler;

	std::vector<std::atomic<count> > maxInternalDeg(C.upperBound());

	handler.assureRunning();

	G.balancedParallelForNodes([&](node u) {
		for (index c : C[u]) {
			count internalDeg = 0;
			G.forNeighborsOf(u, [&](node v) {
				if (C[v].count(c) > 0) {
					internalDeg++;
				}
			});

			Aux::Parallel::atomic_max(maxInternalDeg[c], internalDeg);
		}
	});

	handler.assureRunning();

	std::vector<count> clusterSizes(C.upperBound(), 0);
	count numMemberships = 0;

	G.forNodes([&](node u) {
		for (index c : C[u]) {
			++clusterSizes[c];
		}

		numMemberships += C[u].size();
	});

	handler.assureRunning();

	unweightedAverage = 0;
	weightedAverage = 0;
	minimumValue = std::numeric_limits<double>::max();
	maximumValue = std::numeric_limits<double>::lowest();
	values.clear();
	values.resize(C.upperBound(), 0);

	count numClusters = 0;

	for (index i = 0; i < C.upperBound(); ++i) {
		if (clusterSizes[i] > 0) {
			++numClusters;

			double dominance = 1;
			if (clusterSizes[i] > 1) {
				dominance = maxInternalDeg[i] * 1.0 / (clusterSizes[i] - 1);
			}

			values[i] = dominance;
			minimumValue = std::min(dominance, minimumValue);
			maximumValue = std::max(dominance, maximumValue);
			unweightedAverage += dominance;
			weightedAverage += dominance * clusterSizes[i];
		}
	}

	handler.assureRunning();

	unweightedAverage /= numClusters;
	weightedAverage /= numMemberships;

	hasRun = true;
}
