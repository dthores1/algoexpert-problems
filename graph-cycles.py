"""
    You're given a list of edges representing an unweighted, directed
    graph with at least one node. Write a function that returns a boolean
    representing whether the given graph contains a cycle.

    For the purpose of this question, a cycle is defined as any number of
    vertices, including just one vertex, that are connected in a closed chain. A
    cycle can also be defined as a chain of at least one vertex in which the first
    vertex is the same as the last.

    The given list is what's called an adjacency list, and it represents a graph.
    The number of vertices in the graph is equal to the length of
    edges, where each index i in edges contains vertex i's outbound edges, in no
    particular order. Each individual edge is represented by a positive integer
    that denotes an index (a destination vertex) in the list that this vertex is
    connected to. Note that these edges are directed, meaning that you can only
    travel from a particular vertex to its destination, not the other way around
    (unless the destination vertex itself has an outbound edge to the original
    vertex).

    Also note that this graph may contain self-loops. A self-loop is an edge that
    has the same destination and origin; in other words, it's an edge that
    connects a vertex to itself. For the purpose of this question, a self-loop is
    considered a cycle.

    For a more detailed explanation, please refer to the Conceptual Overview
    section of this question's video explanation.

    Example:
        edges = [
            [1, 3],
            [2, 3, 4],
            [0],
            [],
            [2, 5],
            []
        ]

    Output:
        True
        // There are multiple cycles in this graph: 
        // 1) 0 -> 1 -> 2 -> 0
        // 2) 0 -> 1 -> 4 -> 2 -> 0
        // 3) 1 -> 2 -> 0 -> 1
        // These are just 3 examples; there are more.
"""
from enum import Enum, auto

def cycleInGraph(edges):
	visit_info = [Status.NOT_STARTED] * len(edges)

	for i in range(len(edges)):
		cycles = dfs_traverse(i, edges, visit_info)
		
		if cycles:
			return True
		
	return False
		
def dfs_traverse(node, edges, visit_info):
	if visit_info[node] == Status.IN_PROGRESS:
		return True
	
	visit_info[node] = Status.IN_PROGRESS
	
	for kid in edges[node]:
		cycles = dfs_traverse(kid, edges, visit_info)
		
		if cycles:
			return True
	
	visit_info[node] = Status.VISITED

class Status(Enum):
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    VISITED = auto()

edges1 = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
]
assert cycleInGraph(edges1)

edges2 = [
    [1, 2],
    [2],
    []
]
assert not cycleInGraph(edges2)

edges3 = [
    [1, 2],
    [2],
    [1]
]
assert cycleInGraph(edges3)

edges4 = [
    [1, 2],
    [2],
    [1, 3],
    [3]
]
assert cycleInGraph(edges4)

edges5 = [
    [],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0]
]
assert(edges5)