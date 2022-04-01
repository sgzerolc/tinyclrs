import unittest

# graph representations
# adjacency list
A1 = [[1],
      [2],
      [0],
      [4],
      []]


# bfs
def bfs(Adj, s):
    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]
    while 0 < len(level[-1]):
        level.append([])
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)
    return parent


def unweighted_shortest_path(Adj, s, t):
    parent = bfs(Adj, s)
    if parent[t] is None:
        return None
    i = t
    path = [t]
    while i != s:
        i = parent[i]
        path.append(i)
    return path[::-1]


# dfs
def dfs(Adj, s, parent=None, order=None):
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
        order = []
    for v in Adj[s]:
        parent[v] = s
        dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order


# print(unweighted_shortest_path(A1, 0, 4))

# relax and weighted graphs
# weighted graph: def w(u,v): return w[u][v]
W1 = {0: {1: -2},
      1: {2: 0},
      2: {0: 1},
      3: {4: 3}}


# general relax
def general_relax(Adj, w, s):
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    # while True:
    # relax() # relax a shortest path estimate d(s,v)
    while some_edge_relaxable(Adj, w, d):  # its implementations depends on real situations
        (u, v) = get_relaxable_edge(Adj, w, d)
        relax(Adj, w, d, parent, u, v)
    return d, parent


def some_edge_relaxable():
    return None


def get_relaxable_edge():
    return None


def relax(Adj, w, d, parent, u, v):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        parent[v] = u


# topological sort relaxation
def DAG_Shortes_Paths(Adj, w, s):
    _, order = dfs(Adj, s)
    order.reverse()
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    for u in order:
        for v in Adj[u]:
            relax(Adj, w, d, parent, u, v)
    return d, parent


# bellman-ford
def bellman_ford(Adj, w, s):
    # initialize source
    infinity = float('inf')
    d = [infinity for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s

    V = len(Adj)
    for i in range(V - 1):
        for u in range(V):
            for v in Adj[u]:
                relax(Adj, w, d, parent, u, v)
    # check for negative weight cycles accessible from s
    for u in range(V):
        for v in Adj[u]:
            if d[v] > d[u] + w(u, v):
                raise Exception('Ack! negative weight cycle!')
    return d, parent


# dijkstra's algorithm
def dijkstra(Adj, w, s):
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    Q = PriorityQueue()
    for v in range(len(Adj)):
        Q.insert(v, d[v])
    for _ in range(len(Adj)):
        u = Q.extract_min()
        for v in Adj[u]:
            relax(Adj, w, d, parent, u, v)
            Q.decrese_key(v, d[v])
    return d, parent


class PriorityQueue():
    def __init__(self):
        self.A = {}


class TestGraph(unittest.TestCase):
    def test_spt_path(self):
        p1 = [0, 0, 1, None, None]
        par = bfs(A1, 0)
        print("parents of A1: ", par)
        self.assertEqual(par, p1)


if __name__ == '__main__':
    unittest.main()
