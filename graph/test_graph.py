import unittest, sys

# go up one level to import modules from other cousin directories
# excution path: python test_graph.py
sys.path.append("..")
from priority_queue.direct_access_arr import PriorityQueue
from sssp import bfs, A1, A2


class TestBFS(unittest.TestCase):
    def test_bfs_basic_connectivity(self):
        """Test BFS on a simple connected graph"""
        # Graph: 0 -> 1 -> 2 -> 3
        Adj = [[1], [2], [3], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, 1, 2]
        self.assertEqual(parent, expected)

    def test_bfs_disconnected_graph(self):
        """Test BFS when there are unreachable vertices"""
        # Graph: 0 -> 1, 2 -> 3 (disconnected components)
        Adj = [[1], [], [3], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, None, None]
        self.assertEqual(parent, expected)

    def test_bfs_single_vertex(self):
        """Test BFS on a graph with just one vertex"""
        Adj = [[]]
        parent = bfs(Adj, 0)
        expected = [0]
        self.assertEqual(parent, expected)

    def test_bfs_linear_path(self):
        """Test BFS on a simple path"""
        # Graph: 0 -> 1 -> 2 -> 3 -> 4
        Adj = [[1], [2], [3], [4], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, 1, 2, 3]
        self.assertEqual(parent, expected)

    def test_bfs_cycle(self):
        """Test BFS on a graph with cycles"""
        # Graph: 0 -> 1 -> 2 -> 0 (cycle)
        Adj = [[1], [2], [0]]
        parent = bfs(Adj, 0)
        expected = [0, 0, 1]
        self.assertEqual(parent, expected)

    def test_bfs_multiple_components(self):
        """Test BFS on a graph with multiple connected components"""
        # Graph: 0 -> 1, 2 -> 3 -> 4, 5 -> 6
        Adj = [[1], [], [3], [4], [], [6], []]
        parent = bfs(Adj, 2)
        expected = [None, None, 2, 2, 3, None, None]
        self.assertEqual(parent, expected)

    def test_bfs_complex_graph(self):
        """Test BFS on a more complex graph"""
        # Using A2: [[1, 3, 4], [0], [3], [0, 2], [0]]
        parent = bfs(A2, 0)
        expected = [0, 0, 3, 0, 0]
        self.assertEqual(parent, expected)

    def test_bfs_start_from_middle(self):
        """Test BFS starting from a vertex in the middle of the graph"""
        # Graph: 0 -> 1 -> 2 -> 3 -> 4
        Adj = [[1], [2], [3], [4], []]
        parent = bfs(Adj, 2)
        expected = [None, None, 2, 2, 3]
        self.assertEqual(parent, expected)

    def test_bfs_empty_adjacency(self):
        """Test BFS on a graph with empty adjacency lists"""
        Adj = [[], [], [], []]
        parent = bfs(Adj, 0)
        expected = [0, None, None, None]
        self.assertEqual(parent, expected)

    def test_bfs_self_loop(self):
        """Test BFS on a graph with self-loops"""
        # Graph: 0 -> 0 (self-loop), 1 -> 2
        Adj = [[0], [2], []]
        parent = bfs(Adj, 0)
        expected = [0, None, None]
        self.assertEqual(parent, expected)

    def test_bfs_bidirectional_edges(self):
        """Test BFS on a graph with bidirectional edges"""
        # Graph: 0 <-> 1 <-> 2
        Adj = [[1], [0, 2], [1]]
        parent = bfs(Adj, 0)
        expected = [0, 0, 1]
        self.assertEqual(parent, expected)

    def test_bfs_existing_a1_graph(self):
        """Test BFS on the existing A1 graph"""
        # A1 = [[1], [2], [0], [4], []]
        parent = bfs(A1, 0)
        expected = [0, 0, 1, None, None]
        self.assertEqual(parent, expected)

    def test_bfs_unreachable_vertices(self):
        """Test BFS when some vertices are unreachable from source"""
        # Graph: 0 -> 1, 2 -> 3 (vertex 2 and 3 unreachable from 0)
        Adj = [[1], [], [3], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, None, None]
        self.assertEqual(parent, expected)

        # Test from vertex 2
        parent = bfs(Adj, 2)
        expected = [None, None, 2, 2]
        self.assertEqual(parent, expected)

    def test_bfs_diamond_graph(self):
        """Test BFS on a diamond-shaped graph"""
        # Graph: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
        Adj = [[1, 2], [3], [3], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, 0, 1]  # or [0, 0, 0, 2] depending on traversal order
        self.assertEqual(parent, expected)

    def test_bfs_star_graph(self):
        """Test BFS on a star graph"""
        # Graph: 0 -> 1, 0 -> 2, 0 -> 3, 0 -> 4
        Adj = [[1, 2, 3, 4], [], [], [], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(parent, expected)

    def test_bfs_tree_structure(self):
        """Test BFS on a tree structure"""
        # Graph: 0 -> 1, 0 -> 2, 1 -> 3, 1 -> 4, 2 -> 5, 2 -> 6
        Adj = [[1, 2], [3, 4], [5, 6], [], [], [], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, 0, 1, 1, 2, 2]
        self.assertEqual(parent, expected)

    def test_bfs_large_graph(self):
        """Test BFS on a larger graph"""
        # Graph with 8 vertices forming a complex structure
        Adj = [[1, 2], [3, 4], [5, 6], [7], [], [], [], []]
        parent = bfs(Adj, 0)
        expected = [0, 0, 0, 1, 1, 2, 2, 3]
        self.assertEqual(parent, expected)


if __name__ == "__main__":
    unittest.main()
