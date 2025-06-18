import unittest, sys

sys.path.append("..")
from priority_queue.direct_access_arr import PriorityQueue

# graph representations
# adjacency list: Adj contains v's outgoing (or incoming) edges. The rows denote vertices which
# form edges with v. The array slot i points to the Adj list of the vertex labled i.
# G1: 0->1->2->0, 3->4
A1 = [[1], [2], [0], [4], []]  # 0  # 1  # 2  # 3  # 4

# G2: 0<->1, 0<->3<->2, 0<->4
A2 = [[1, 3, 4], [0], [3], [0, 2], [0]]

# G3: 0->1->3, 0->2->3
# Possible multiple shortest paths
A3 = [[1, 2], [3], [3], []]


# detect cycles in undirected graphs
def is_cyclic(Adj):
    pass  # TODO: implement cycle detection


# BFS: explore level by level (level sets of source vertex s)
# Construct a BFS tree from an unweighted graph.
# Run time: O(|V| + |E|), O(sum(deg(v))) + O(len(parent))
def bfs(Adj, s):
    """
    Breadth-first search for a graph represented by an index-labeled adjacency list.

    :return: a parent label for each vertex in the direction of a shortest path back to s.
    For example, for the edge 0->1, the parent of 1 is 0.
    """
    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]
    while 0 < len(level[-1]):
        level.append([])
        # Traverse the last full level.
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    # The parent of the vertex in the Adj list of s is s.
                    parent[v] = u
                    level[-1].append(v)
    print("level: ", level)
    print("parent: ", parent)
    return parent


def bfs_all(Adj, s):
    n = len(Adj)
    parents = [[] for _ in range(n)]
    distances = [float("inf") for _ in range(n)]

    parents[s] = [s]  # Source is its own parent
    distances[s] = 0

    # BFS queue: (vertex, distance)
    # queue = [(s, 0)]
    level = [[(s, 0)]]
    visited = set([s])

    while 0 < len(level[-1]):
        # queue.pop(0)
        level.append([])

        for u, dist in level[-2]:
            for v in Adj[u]:
                # use distances to check if a path has been discovered
                if distances[v] == float("inf"):
                    distances[v] = dist + 1
                    parents[v] = [u]
                    # quue.append(v, dist + 1)
                    level[-1].append((v, dist + 1))
                    visited.add(v)
                elif distances[v] == dist + 1:
                    parents[v].append(u)

    return parents, distances


def find_all_path(Adj, s, t):
    parents, distances = bfs_all(Adj, s)

    if distances[t] == float("inf"):
        return []

    def reconstruct(v, sub_path):
        """Recursively reconstruct all paths from s to v."""
        if v == s:
            return [sub_path[::-1]]  # Reverse the path since we built it backwards

        all_paths = []
        for u in parents[v]:
            path = sub_path + [u]
            all_paths.extend(reconstruct(u, path))

        return all_paths

    return reconstruct(t, [t])


def unweighted_shortest_path(Adj, s, t):
    parent, _ = dfs(Adj, s)
    if parent[t] is None:
        return None
    i = t
    path = [t]
    while i != s:
        i = parent[i]
        path.append(i)
    return path[::-1]


# DFS
# Construct a DFS tree in the order of searching from DAG.
# Relax in order.
def dfs(Adj, s, parent=None, order=None):
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
        order = []
    for v in Adj[s]:
        parent[v] = s
        dfs(Adj, v, parent, order)
    # A reverse order of searching is a topological sort order.
    order.append(s)
    print("parent: ", parent, "s: ", s)
    print("order: ", order)
    return parent, order


def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in Adj:
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order


# relax and weighted graphs
# weighted graph:
W1 = {0: {1: -2}, 1: {2: 0}, 2: {0: 1}, 3: {4: 3}}

W3 = {0: {1: 2, 2: 3}, 1: {3: 4}, 2: {3: 2}, 3: {}}


# general relax
def general_relax(Adj, w, s):
    d = [float("inf") for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    # while True:
    # relax() # relax a shortest path estimate d(s,v)
    while some_edge_relaxable(
        Adj, w, d
    ):  # its implementations depends on real situations
        (u, v) = get_relaxable_edge(Adj, w, d)
        relax(Adj, w, d, parent, u, v)
    return d, parent


def some_edge_relaxable():
    return None


def get_relaxable_edge():
    return None


def get_w(w, u, v):
    return w[u][v]


def relax(Adj, w, d, parent, u, v):
    if d[v] > d[u] + get_w(w, u, v):
        d[v] = d[u] + get_w(w, u, v)
        parent[v] = u  # u->v


# topological sort relaxation
def DAG_Shortes_Paths(Adj, w, s):
    _, order = dfs(Adj, s)
    order.reverse()
    d = [float("inf") for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    for u in order:
        for v in Adj[u]:
            relax(Adj, w, d, parent, u, v)
    print("d: ", d)
    print("parent: ", parent)
    return d, parent


# bellman-ford
def bellman_ford(Adj, w, s):
    # initialize source
    infinity = float("inf")
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
                raise Exception("Ack! negative weight cycle!")
    return d, parent


# dijkstra's algorithm
def dijkstra(Adj, w, s):
    d = [float("inf") for _ in Adj]
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


def prim(Adj, w, V):
    Q = PriorityQueue()
    S = set()  # S is empty first
    parent = [None for _ in Adj]
    # cut, least weight edge
    s = V[-1]  # for arbitrary start vertex
    Q.insert(s, 0)
    for v in V[:-1]:
        Q.insert(v, float("inf"))

    while Q:
        u = Q.extract_min()
        S.add(u)
        for v in Adj[u]:
            if v in Q and v not in S and w(u, v) < Q[v]:  # v.key
                Q.decrease_key(v, w(u, v))  # v.key = w(u, v)
                parent[v] = u  # v.parent = u
    return [(v, parent[v]) for v in V[:-1]]


if __name__ == "__main__":
    # print("From 0 to 4 in A1: ", unweighted_shortest_path(A1, 0, 4))
    # print("From 0 to 2 in A2: ", unweighted_shortest_path(A2, 0, 2))
    # print("From 0 to 3 in A3: ", unweighted_shortest_path(A3, 0, 3))

    # print("\n--- All Shortest Paths ---")
    # print("From 0 to 3 in A3:")
    # all_paths = find_all_path(A3, 0, 3)
    # for i, path in enumerate(all_paths):
    #    print(f"  Path {i+1}: {path}")

    # print("\nFrom 0 to 2 in A2:")
    # all_paths = find_all_path(A2, 0, 2)
    # for i, path in enumerate(all_paths):
    #    print(f"  Path {i+1}: {path}")

    # topological sort
    print("From 0 to 3 in A3: ", unweighted_shortest_path(A3, 0, 3))

    # DAG shortest paths
    print("DAG shortest paths: ", DAG_Shortes_Paths(A3, W3, 0))
