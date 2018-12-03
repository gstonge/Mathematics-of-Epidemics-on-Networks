# -*- coding: utf-8 -*-
"""
This module provides classes and methods to perform efficient SIS simulations
using the event-driven approach.
"""

import networkx
import numpy as np
from random import random

__author__ = "Guillaume St-Onge"
__copyright__ = "Copyright (c) 2018 Guillaume St-Onge"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "guillaume.st-onge.4@ulaval.ca"
__status__ = "development"

class NeighborSampler:
    """Class to sample the neighbors of a node proportionally to their
    weights, if specified.
    """
    def __init__(self, G):
        self.neighbor_cumulative_weight_list_dict = dict()
        self.neighbor_label_list_dict = dict()
        #initialize the dictionaries
        for u in G:
            self.neighbor_label_list_dict[u] = list(G.neighbors(u))
            #calculate the neighbor cumulative weight list for each node
            self.neighbor_cumulative_weight_list_dict[u] = [0]
            l = self.neighbor_cumulative_weight_list_dict[u]
            for v in G.neighbors(u):
                if "weight" in G.get_edge_data(u,v):
                    l.append(l[-1] + G.get_edge_data(u,v)["weight"])
                else:
                    l.append(l[-1] + 1) #default weight is 1 for each edge
            l.pop(0)
            l = np.array(l)

    def get_total_weight(self, node):
        """Returns the sum of the edge weights for all neighbors of a node."""
        return self.neighbor_cumulative_weight_list_dict[node][-1]

    def get_random_neighbor(self, node):
        """Returns a random neighbor of a node according to the edge weight."""
        l = self.neighbor_cumulative_weight_list_dict[node]
        w = random()*l[-1]
        index = np.searchsorted(l,w)
        return self.neighbor_label_list_dict[node][index]


def _get_efficient_trans_and_rec_fxn_(G, cumulative_trans_fxn,
                                      inverse_cumulative_trans_fxn,
                                      inverse_cumulative_rec_fxn):
    """Returns efficient methods to determine the transmission to neighbors
    and arguments to be used along with fast_nonMarkov_SIS.
    """
    pass

