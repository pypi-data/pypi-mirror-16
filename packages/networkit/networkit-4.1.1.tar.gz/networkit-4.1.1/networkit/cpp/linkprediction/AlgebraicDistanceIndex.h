/*
 * AlgebraicDistanceIndex.h
 *
 *  Created on: 19.06.2013
 *      Authors: cls, Kolja Esders
 */

#ifndef ALGEBRAICDISTANCEINDEX_H_
#define ALGEBRAICDISTANCEINDEX_H_

#include "LinkPredictor.h"
#include "../graph/Graph.h"
#include "../auxiliary/Timer.h"


namespace NetworKit {

/**
 * @ingroup linkprediction
 *
 * Algebraic distance assigns a distance value to pairs of nodes
 * according to their structural closeness in the graph. 
 */
class AlgebraicDistanceIndex : public LinkPredictor {
private:

	/**
	 * Returns the extended algebraic distance between node @a u and node @a v in the norm specified in
	 * the constructor.
	 * @param u The first node
	 * @param v The second node
	 * @return Extended algebraic distance between the two nodes.
	 */
	double runImpl(node u, node v) override;

protected:
	count numSystems; //!< number of vectors/systems used for algebraic iteration
	count numIters; //!< number of iterations in each system
	double omega; //!<
	index norm;
	const index MAX_NORM = 0;

	std::vector<std::vector<double> > loads; //!< loads[i]: vector of loads of length n for one system

	void randomInit();

public:
	explicit AlgebraicDistanceIndex(count numberSystems, count numberIterations, double omega = 0.5, index norm = 2);

	/**
	 * @param G The graph.
	 * @param numberSystems Number of vectors/systems used for algebraic iteration.
	 * @param numberIterations Number of iterations in each system.
	 * @param omega Overrelaxation parameter.
	 * @param norm The norm factor of the extended algebraic distance. Maximum norm is realized by setting @a norm to 0.
	 */
	explicit AlgebraicDistanceIndex(const Graph& G, count numberSystems, count numberIterations, double omega = 0.5, index norm = 2);

	/**
	 * Starting with random initialization, compute for all @a numberSystems
	 * "diffusion" systems the situation after @a numberIterations iterations
	 * of overrelaxation with overrelaxation parameter @a omega.
	 *
	 * REQ: Needs to be called before algdist delivers meaningful results!
	 */
	 virtual void preprocess();
	 
};

} /* namespace NetworKit */
#endif /* ALGEBRAICDISTANCEINDEX_H_ */
