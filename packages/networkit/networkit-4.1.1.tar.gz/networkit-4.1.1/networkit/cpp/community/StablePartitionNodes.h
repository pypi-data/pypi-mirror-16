#ifndef STABLEPARTITIONNODES_H
#define STABLEPARTITIONNODES_H

#include "LocalPartitionEvaluation.h"

namespace NetworKit {

/**
 * Evaluates how stable a given partition is. A node is considered to be stable if it has strictly more connections
 * to its own partition than to other partitions. Isolated nodes are considered to be stable.
 * The value of a cluster is the percentage of stable nodes in the cluster.
 * Larger values indicate that a clustering is more stable and thus better defined.
 */
class StablePartitionNodes : public LocalPartitionEvaluation {
public:
	using LocalPartitionEvaluation::LocalPartitionEvaluation; // inherit constructor

	/**
	 * Execute the algorithm.
	 */
	virtual void run() override;

	/**
	 * Check if a given node is stable, i.e. more connected to its own partition than to other partitions.
	 *
	 * @param u The node to check
	 * @return If the node @a u is stable.
	 */
	bool isStable(node u) const { assureFinished(); return static_cast<bool>(stableMarker[u]); };

	/**
	 * If small values are better. Here large values are better.
	 *
	 * @return false.
	 */
	virtual bool isSmallBetter() const override { return false; }
private:
	std::vector<uint8_t> stableMarker;
};

}

#endif // STABLEPARTITIONNODES_H
