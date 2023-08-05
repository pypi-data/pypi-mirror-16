/*
 * GeometricMeanScore.h
 *
 *  Created on: 20.11.2014
 *      Author: Michael Hamann
 */

#include <cmath>
#include "GeometricMeanScore.h"
#include "../auxiliary/Log.h"

namespace NetworKit {

GeometricMeanScore::GeometricMeanScore(const Graph& G, const std::vector<double>& attribute): EdgeScore<double>(G), attribute(attribute) {
}

void GeometricMeanScore::run() {
	if (!G.hasEdgeIds()) {
		throw std::runtime_error("edges have not been indexed - call indexEdges first");
	}

	scoreData.resize(G.upperEdgeIdBound());
	
	std::vector<double> nodeSum(G.upperNodeIdBound());
	
	G.parallelForNodes([&](node u) {
		G.forEdgesOf(u, [&](node _u, node v, edgeid eid) {
			nodeSum[u] += attribute[eid];
		});
	});
	
	G.parallelForEdges([&](node u, node v, edgeid eid) {
		if (attribute[eid] > 0) {
			scoreData[eid] = attribute[eid] * 1.0 / std::sqrt(nodeSum[u] * nodeSum[v]);
			if (std::isnan(scoreData[eid])) {
				ERROR("Attribute ", attribute[eid], " couldn't be normalized with sum ", nodeSum[u], " and sum ", nodeSum[v]);
			}
		}
	});
	
	hasRun = true;
}

double GeometricMeanScore::score(node u, node v) {
	throw std::runtime_error("Not implemented: Use scores() instead.");
}

double GeometricMeanScore::score(edgeid eid) {
	throw std::runtime_error("Not implemented: Use scores() instead.");
}

} /* namespace NetworKit */
