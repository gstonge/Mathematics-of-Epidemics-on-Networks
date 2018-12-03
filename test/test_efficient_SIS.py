import unittest
import EoN
import networkx as nx

class TestNeighborSampler(unittest.TestCase):
    def setUp(self):
        self.unweighted_graph = nx.Graph()
        self.unweighted_graph.add_edge('a', 'b')
        self.unweighted_graph.add_edge('a', 'c')
        self.unweighted_graph.add_edge('c', 'd')
        self.unweighted_graph.add_edge('c', 'e')
        self.unweighted_graph.add_edge('c', 'f')
        self.unweighted_graph.add_edge('a', 'd')

        self.weighted_graph = nx.Graph()
        self.weighted_graph.add_edge('a', 'b', weight=0.6)
        self.weighted_graph.add_edge('a', 'c', weight=0.2)
        self.weighted_graph.add_edge('c', 'd', weight=0.1)
        self.weighted_graph.add_edge('c', 'e', weight=0.7)
        self.weighted_graph.add_edge('c', 'f', weight=0.9)
        self.weighted_graph.add_edge('a', 'd', weight=0.3)

    def test_init_unweighted_graph(self):
        try:
            sampler = EoN.NeighborSampler(self.unweighted_graph)
        except Exception:
            self.fail("An exception is raised")

    def test_init_weighted_graph(self):
        try:
            sampler = EoN.NeighborSampler(self.weighted_graph)
        except Exception:
            self.fail("An exception is raised")

    def test_get_total_weight_unweighted_graph(self):
        sampler = EoN.NeighborSampler(self.unweighted_graph)
        self.assertEqual(sampler.get_total_weight('a'), 3)

    def test_get_total_weight_weighted_graph(self):
        sampler = EoN.NeighborSampler(self.weighted_graph)
        self.assertEqual(sampler.get_total_weight('a'), 1.1)

    def test_get_random_neighbor_unweighted_graph(self):
        sampler = EoN.NeighborSampler(self.unweighted_graph)
        #test multiple times
        for i in range(10):
            self.assertTrue(sampler.get_random_neighbor('a') in ['b','c','d'])

    def test_get_random_neighbor_weighted_graph(self):
        sampler = EoN.NeighborSampler(self.weighted_graph)
        #test multiple times
        for i in range(10):
            self.assertTrue(sampler.get_random_neighbor('a') in ['b','c','d'])


#Test NeighborSampler class
suite = unittest.TestLoader().loadTestsFromTestCase(TestNeighborSampler)
unittest.TextTestRunner(verbosity=2).run(suite)

