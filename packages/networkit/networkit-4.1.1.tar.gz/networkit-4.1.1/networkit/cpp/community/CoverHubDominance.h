#ifndef COVERHUBDOMINANCE_H
#define COVERHUBDOMINANCE_H

#include "LocalCoverEvaluation.h"

namespace NetworKit {

/**
 * A quality measure that measures the dominance of hubs in clusters. The hub dominance of a single
 * cluster is defined as the maximum cluster-internal degree of a node in that cluster divided by
 * the maximum cluster-internal degree, i.e. the number of nodes in the cluster minus one. The
 * value for all clusters is defined as the average of all clusters.
 * This implementation is a natural generalization of this measure for covers.
 * Strictly speaking this is not a quality measure as this is rather dependent on the type of the
 * considered graph, for more information see
 * Lancichinetti A, Kivelä M, Saramäki J, Fortunato S (2010)
 * Characterizing the Community Structure of Complex Networks
 * PLoS ONE 5(8): e11976. doi: 10.1371/journal.pone.0011976
 * http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0011976
 */
class CoverHubDominance : public LocalCoverEvaluation {
public:
	using LocalCoverEvaluation::LocalCoverEvaluation;

	/**
	 * Execute the algorithm.
	 */
	virtual void run() override;

	/**
	 * @return false - smaller is not better, larger values indicate better cluster cohesion.
	 */
	virtual bool isSmallBetter() const override { return false; }

	/**
	 * @return true - this algorithm is partially parallel (but \f$\Omega(n)\f$ sequential work remains)
	 */
	virtual bool isParallel() const override { return true; }
};

}

#endif // COVERHUBDOMINANCE_H
