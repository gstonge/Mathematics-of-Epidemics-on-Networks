# -*- coding: utf-8 -*-
"""
Test script for the simulation of the SIS model using improved
trans_and_rec_time_fxn.
"""

import EoN
import networkx as nx
import matplotlib.pyplot as plt

G = nx.fast_gnp_random_graph(1000, 0.01)
k = 1.
beta = 0.12
alpha = 1.
cumulative_trans_fxn = lambda t: (beta*t)**k
inverse_cumulative_trans_fxn = lambda x: x**(1/k)/beta
inverse_cumulative_rec_fxn = lambda x: x/alpha
initial_inf_count = 10
tmax = 100

trans_and_rec_time_fxn, trans_and_rec_time_args = \
        EoN.get_efficient_trans_and_rec_fxn_SIS(G, cumulative_trans_fxn,
                                                inverse_cumulative_trans_fxn,
                                                inverse_cumulative_rec_fxn)

t, S, I = EoN.fast_nonMarkov_SIS(G,
                   trans_and_rec_time_fxn=trans_and_rec_time_fxn,
                   trans_and_rec_time_args=trans_and_rec_time_args,
                   initial_infecteds=range(initial_inf_count),
                   tmin=0, tmax=tmax)

plt.plot(t,I/len(G))
plt.show()
