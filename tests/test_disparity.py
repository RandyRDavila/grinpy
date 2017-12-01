from grinpy import grinpy as gp


class TestDisparity():
    def setup_class(self):
        G = gp.Graph()
        G.add_edge(0, 1)
        G.add_edge(0, 2)
        G.add_edge(1, 2)
        G.add_edge(0, 3)
        G.add_edge(3, 4)
        G.add_edge(3, 5)
        self.G = G

    def test_vertex_disparity(self):
        G = self.G
        assert(gp.vertex_disparity(G, 0) == 2)
        assert(gp.vertex_disparity(G, 1) == 2)
        assert(gp.vertex_disparity(G, 2) == 2)
        assert(gp.vertex_disparity(G, 3) == 2)
        assert(gp.vertex_disparity(G, 4) == 1)
        assert(gp.vertex_disparity(G, 5) == 1)

    def test_closed_vertex_disparity(self):
        G = self.G
        assert(gp.closed_vertex_disparity(G, 0) == 2)
        assert(gp.closed_vertex_disparity(G, 1) == 2)
        assert(gp.closed_vertex_disparity(G, 2) == 2)
        assert(gp.closed_vertex_disparity(G, 3) == 2)
        assert(gp.closed_vertex_disparity(G, 4) == 2)
        assert(gp.closed_vertex_disparity(G, 5) == 2)

    def test_disparity_sequence(self):
        G = self.G
        assert(gp.disparity_sequence(G) == [2, 2, 2, 2, 1, 1])

    def test_closed_disparity_sequence(self):
        G = self.G
        assert(gp.closed_disparity_sequence(G) == [2, 2, 2, 2, 2, 2])

    def test_CW_disparity(self):
        G = self.G
        assert(gp.CW_disparity(G) == sum([1/3, 1/3, 1/3, 1/3, 1/2, 1/2]))

    def test_closed_CW_disparity(self):
        G = self.G
        assert(gp.closed_CW_disparity(G) == sum([1/3, 1/3, 1/3, 1/3, 1/3, 1/3]))

    def test_inverse_disparity(self):
        G = self.G
        assert(gp.inverse_disparity(G) == sum([1/2, 1/2, 1/2, 1/2, 1/1, 1/1]))

    def test_closed_inverse_disparity(self):
        G = self.G
        assert(gp.closed_inverse_disparity(G) == sum([1/2, 1/2, 1/2, 1/2, 1/2, 1/2]))

    def test_average_vertex_disparity(self):
        G = self.G
        assert(gp.average_vertex_disparity(G) == 10 / 6)

    def test_average_closed_vertex_disparity(self):
        G = self.G
        assert(gp.average_closed_vertex_disparity(G) == 2.0)

    def test_k_disparity(self):
        G = self.G
        assert(gp.k_disparity(G, 1) == 2.0)
        assert(gp.k_disparity(G, 2) == 2.0)
        assert(gp.k_disparity(G, 3) == 2.0)
        assert(gp.k_disparity(G, 4) == 2.0)
        assert(gp.k_disparity(G, 5) == 29 / 15)
        assert(gp.k_disparity(G, 6) == 39 / 21)
