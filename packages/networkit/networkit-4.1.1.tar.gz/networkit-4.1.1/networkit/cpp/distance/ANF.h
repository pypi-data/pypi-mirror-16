#include "../graph/Graph.h"
#include "omp.h"
#include "../auxiliary/Log.h"

namespace NetworKit {

namespace ANF {

/*void initSeq(const Graph& G, std::vector<count>& highestCount, std::vector<std::vector<count> >& mPrev, std::vector<std::vector<count> >& mCurr, count k, count r) {
	// initialize all vectors
	G.forNodes([&](node v) {
		std::vector<count> bitmasks;
		bitmasks.assign(k, 0);
		mCurr.push_back(bitmasks);
		mPrev.push_back(bitmasks);
		activeNodes.push_back(v);
		// set one bit in each bitmask with probability P(bit i=1) = 0.5^(i+1), i=0,..
		for (count j = 0; j < k; j++) {
			double random = Aux::Random::real(0,1);
			count position = ceil(log(random)/log(0.5) - 1);
			// set the bit in the bitmask
			if (position < lengthOfBitmask+r) {
				mPrev[v][j] |= 1 << position;
			}
			// add the current bit to the maximum-bitmask
			highestCount[j] = highestCount[j] | mPrev[v][j];
		}
	});
}


void initPar(const Graph& G, std::vector<count>& highestCount, std::vector<std::vector<count> >& mPrev, std::vector<std::vector<count> >& mCurr, count k, count r) {
	// initialize all vectors
	highestCount.assign(k, 0);
	std::vector<std::vector<count>> localHighest(omp_get_max_threads(), std::vector<count>(k, 0));

	G.parallelForNodes([&](node v) {
		count c = 0;
		std::vector<count> bitmasks;
		bitmasks.assign(k, 0);
		mCurr[v] = bitmasks;
		mPrev[v] = bitmasks;
		activeNodes[v] = 1;
		// set one bit in each bitmask with probability P(bit i=1) = 0.5^(i+1), i=0,..
		std::stringstream ss;
		for (count j = 0; j < k; j++) {
			double random = Aux::Random::real(0,1);
			count position = ceil(log(random)/log(0.5) - 1);
			ss << position << ", ";
			//count position = init_pos[v*k + c++];
			// set the bit in the bitmask
			if (position < lengthOfBitmask) {
				mPrev[v][j] = 1 << position;
			}
			// add the current bit to the maximum-bitmask
			localHighest[omp_get_thread_num()][j] |= mPrev[v][j];
			highestCount[j] |= mPrev[v][j];
		}
		std::cout << ss.str() << std::endl;
	});
	std::vector<count> highestCount2(k,0);
	#pragma omp parallel for
	for (size_t i = 0; i < k; ++i) {
		count tmp = 0;
		#pragma omp parallel for reduction (|:tmp)
		for (ssize_t t = 0; t < omp_get_max_threads(); ++t) {
			tmp |= localHighest[t][i];
		}
		highestCount2[i] = tmp;
	}
	for (size_t i = 0; i < k; ++i) {
		if (highestCount[i] != highestCount2[i]) 
			std::cout << "not the same highest count for\t" << i << "\tdiff:\t" << (highestCount[i] - highestCount2[i]) << std::endl;
	}
	highestCount = highestCount2;
}*/

double sequential(const Graph& G, const double ratio=0.9, const count k=64, const count r=7) {
	count z = G.upperNodeIdBound();
	// the length of the bitmask where the number of connected nodes is saved
	count lengthOfBitmask = (count) ceil(log2(G.numberOfNodes()));
	// saves all k bitmasks for every node of the current iteration
	std::vector<std::vector<count> > mCurr(z);
	// saves all k bitmasks for every node of the previous iteration
	std::vector<std::vector<count> > mPrev(z);
	// the maximum possible bitmask based on the random initialization of all k bitmasks
	std::vector<count> highestCount(k, 0);
	// the amount of nodes that need to be connected to all others nodes
	count threshold = (count) (ceil(ratio * G.numberOfNodes()));
	// the current distance of the neighborhoods
	count h = 1;
	// sums over the number of edges needed to reach 90% of all other nodes
	double effectiveDiameter = 0;
	// the estimated number of connected nodes
	double estimatedConnectedNodes;
	// used for setting a random bit in the bitmasks
	double random;
	// the position of the bit that has been set in a bitmask
	count position;
	// nodes that are not connected to enough nodes yet
	std::vector<node> activeNodes;

	// initialize all vectors
	highestCount.assign(k, 0);
	G.forNodes([&](node v) {
		std::vector<count> bitmasks(k, 0);
		mCurr[v] = bitmasks;
		mPrev[v] = bitmasks;
		activeNodes.push_back(v);
		// set one bit in each bitmask with probability P(bit i=1) = 0.5^(i+1), i=0,..
		for (count j = 0; j < k; j++) {
			random = Aux::Random::real(0,1);
			position = ceil(log(random)/log(0.5) - 1);
			// set the bit in the bitmask
			if (position < lengthOfBitmask+r) {
				mPrev[v][j] |= 1 << position;
			}
			// add the current bit to the maximum-bitmask
			highestCount[j] = highestCount[j] | mPrev[v][j];
		}
	});

	// as long as we need to connect more nodes
	while (!activeNodes.empty()) {
		count proc_nodes = 0;
		//std::cout << "queued:\t" << activeNodes.size();
		for (count x = 0; x < activeNodes.size();) {
			node v = activeNodes[x];
			++proc_nodes;
			#pragma omp parallel for
			// for each parallel approximation
			for (count j = 0; j < k; j++) {
				// the node is still connected to all previous neighbors
				mCurr[v][j] = mPrev[v][j];
				// and to all previous neighbors of all its neighbors
				G.forNeighborsOf(v, [&](node u) {
					mCurr[v][j] = mCurr[v][j] | mPrev[u][j];
				});
			}

			// the least bit number in the bitmask of the current node/distance that has not been set
			double b = 0;

			for (count j = 0; j < k; j++) {
				for (count i = 0; i < sizeof(i)*8; i++) {
					if (((mCurr[v][j] >> i) & 1) == 0) {
						b += i;
						break;
					}
				}
			}
			// calculate the average least bit number that has not been set over all parallel approximations
			b = b / k;

			// calculate the estimated number of neighbors where 0.77351 is a correction factor and the result of a complex sum
			estimatedConnectedNodes = (pow(2,b) / 0.77351);

			// check whether all k bitmask for this node have reached their highest possible value
			bool nodeFinished = true;
			for (count j = 0; j < k; j++) {
				if (mCurr[v][j] != highestCount[j]) {
					nodeFinished = false;
					break;
				}
			}
			// if the node wont change or is connected to enough nodes it must no longer be considered
			if (estimatedConnectedNodes >= threshold || nodeFinished) {
				effectiveDiameter += h;
				// remove the current node from future iterations
				std::swap(activeNodes[x], activeNodes.back());
				activeNodes.pop_back();
			} else {
				++x;
			}
		}
		//std::cout << "\tprocessed:\t" << proc_nodes << std::endl;
		mPrev = mCurr;
		h++;
	}
	return effectiveDiameter/G.numberOfNodes();
}

double parallel(const Graph& G, const double ratio=0.9, const count k=64, const count r=7) {
		// the length of the bitmask where the number of connected nodes is saved
		const count lengthOfBitmask = (count) ceil(log2(G.numberOfNodes())) + r;
		// saves all k bitmasks for every node of the current iteration
		std::vector<std::vector<count> > mCurr(G.upperNodeIdBound());
		// saves all k bitmasks for every node of the previous iteration
		std::vector<std::vector<count> > mPrev(G.upperNodeIdBound());
		// the list of nodes that are already connected to all other nodes
		std::vector<count> highestCount;
		// the amount of nodes that need to be connected to all others nodes
		const count threshold = (count) (ceil(ratio * G.numberOfNodes()));
		// the current distance of the neighborhoods
		count h = 1;
		// sums over the number of edges needed to reach 90% of all other nodes
		double effectiveDiameter = 0;
		// nodes that are not connected to enough nodes yet
		std::vector<char> activeNodes(G.upperNodeIdBound(),0);

		// initialize all vectors
		highestCount.assign(k, 0);
		std::vector<std::vector<count>> localHighest(omp_get_max_threads(), std::vector<count>(k, 0));

		omp_set_nested(1);
		Aux::Random::setSeed(0, true);
		G.parallelForNodes([&](node v) {
			//count c = 0;
			std::vector<count> bitmasks;
			bitmasks.assign(k, 0);
			mCurr[v] = bitmasks;
			mPrev[v] = bitmasks;
			activeNodes[v] = 1;
			// set one bit in each bitmask with probability P(bit i=1) = 0.5^(i+1), i=0,..
			for (count j = 0; j < k; j++) {
				double random = Aux::Random::real(0,1);
				count position = ceil(log(random)/log(0.5) - 1);
				// set the bit in the bitmask
				if (position < lengthOfBitmask) {
					mPrev[v][j] = 1 << position;
				}
				// add the current bit to the maximum-bitmask
				localHighest[omp_get_thread_num()][j] |= mPrev[v][j];
				highestCount[j] |= mPrev[v][j];
			}
		});
		std::vector<count> highestCount2(k,0);
		#pragma omp parallel for
		for (size_t i = 0; i < k; ++i) {
			count tmp = 0;
			#pragma omp parallel for reduction (|:tmp)
			for (ssize_t t = 0; t < omp_get_max_threads(); ++t) {
				tmp |= localHighest[t][i];
			}
			highestCount2[i] = tmp;
		}
		for (size_t i = 0; i < k; ++i) {
			if (highestCount[i] != highestCount2[i]) 
				WARN("not the same highest count for\t", i, "\tdiff:", (highestCount[i] - highestCount2[i]), "\t: ", highestCount[i], "\t: ", highestCount2[i]);
				//std::cout << "not the same highest count for\t" << i << "\tdiff:" << (highestCount[i] - highestCount2[i]) << "\t: " << highestCount[i] << "\t: " << highestCount2[i] << std::endl;
		}
		highestCount = highestCount2;

		std::vector<count> localEffDia(omp_get_max_threads(), 0);
		std::vector<std::vector<node>> localNext(omp_get_max_threads(), std::vector<node>());
		// as long as we need to connect more nodes
		
		bool queued = true;
		while (queued) {
			//count c = 0;
			queued = false;
			//count proc_nodes = 0;
			#pragma omp parallel for schedule(guided) 
			for (count v = 0; v < activeNodes.size(); ++v) {
				if (!activeNodes[v]) continue;
				//++proc_nodes;
				// for each parallel approximation
				for (count j = 0; j < k; j++) {
					// the node is still connected to all previous neighbors
					mCurr[v][j] = mPrev[v][j];
					// and to all previous neighbors of all its neighbors
					G.forNeighborsOf(v, [&](node u) {
						mCurr[v][j] |= mPrev[u][j];
					});
				}

				// the least bit number in the bitmask of the current node/distance that has not been set
				double b = 0;

				for (count j = 0; j < k; j++) {
					for (count i = 0; i < sizeof(i)*8; i++) {
						if (((mCurr[v][j] >> i) & 1) == 0) {
							b += i;
							break;
						}
					}
				}
				// calculate the average least bit number that has not been set over all parallel approximations
				b = b / k;
				// calculate the estimated number of neighbors where 0.77351 is a correction factor and the result of a complex sum
				double estimatedConnectedNodes = (pow(2,b) / 0.77351);
				//std::cout << "(" << v << ", " << estimatedConnectedNodes << ")\t";


				// check whether all k bitmask for this node have reached their highest possible value
				bool nodeFinished = true;
				for (count j = 0; j < k; j++) {
					if (mCurr[v][j] != highestCount[j]) {
						nodeFinished = false;
						break;
					}
				}
				// if the node wont change or is connected to enough nodes it must no longer be considered
				if (estimatedConnectedNodes >= threshold || nodeFinished) {
					localEffDia[omp_get_thread_num()] += h;
					//effectiveDiameter += h;
					// remove the current node from future iterations
					//std::swap(activeNodes[x], activeNodes.back());
					//activeNodes.pop_back();
					activeNodes[v] = 0;
					//#pragma omp atomic
					//++c;
				} else {
					//localNext[omp_get_thread_num()].push_back(v);
					queued = true;
				}
			}
			//std::cout << std::endl;
			/*count sum = 0;
			for (auto& n : localNext) {
				sum += n.size();
				n.clear();
			}*/
			//INFO("activeNodes.size():\t",activeNodes.size(),"\tsum of nodes added:\t",sum);
			//std::cout << "processed:\t" << proc_nodes << std::endl;
			//std::cout << "finished nodes in level " << h << ":\t" << c << std::endl;
			mPrev = mCurr;
			h++;
		}
		#pragma omp parallel for reduction (+:effectiveDiameter)
		for (ssize_t i = 0; i < omp_get_max_threads(); ++i) {
			//INFO("localEffDia[",i,"]:\t",localEffDia[i]);
			effectiveDiameter += localEffDia[i];
		}
		return effectiveDiameter/G.numberOfNodes();
	};

}

}