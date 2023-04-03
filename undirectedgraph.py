# Playing around with undirected graphs.
import collections
from typing import Any


class UndirectedGraph:
    """An undirected graph."""

    def __init__(self):
        self.nodes = set()
        self.edges = set()
        self.edge_map = collections.defaultdict(list)

    class Node:
        """A node with a value."""

        def __init__(self, value: Any):
            self.value = value

        def __str__(self):
            return self.value

    class Edge:
        """An edge connecting two nodes."""

        def __init__(self, left: "Node", right: "Node"):
            self.left = left
            self.right = right

        def __str__(self):
            return self.left + " -- " + self.right

    def add_nodes(self, nodes_list):
        self.nodes.update(nodes_list)

    def add_edges(self, edges_list):
        self.edges.update(edges_list)

        for edge in edges_list:
            self.edge_map[edge.left].append(edge.right)
            self.edge_map[edge.right].append(edge.left)

    def __str__(self):
        string_repr = ["\n"]
        for node in self.nodes:
            string_repr.append("{}".format(node.value))
            edge_dests = self.edge_map[node]
            if not edge_dests:
                string_repr.append("    No outgoing edges")
            for dest in edge_dests:
                string_repr.append("    -> {}".format(dest.value))

        return "\n".join(string_repr)


def disjoint(graph: UndirectedGraph) -> bool:
    """Check if the given graph is disjoint.

    In an undirected graph this is relatively simple. I do a BFS and check
    at the end if visited nodes == all graph nodes.
    """
    if not graph.nodes:
        return False

    visited = set()
    next_to_visit = collections.deque()

    # Pick the first node in the graph and start traversing from there.
    # Doing the pop and add is kind of a pain, but I dunno, it's easier than
    # trying to peek since sets don't really support it.
    starter_node = graph.nodes.pop()
    graph.nodes.add(starter_node)
    visited.add(starter_node)
    for dest in graph.edge_map[starter_node]:
        next_to_visit.append(dest)
    while len(next_to_visit) > 0:
        to_visit = next_to_visit.pop()
        visited.add(to_visit)
        for dest in graph.edge_map[to_visit]:
            if dest not in visited:
                next_to_visit.append(dest)
    return False if len(visited) == len(graph.nodes) else True


if __name__ == "__main__":
    node_map = {}
    for i in range(7):
        node_map[i] = UndirectedGraph.Node(str(i))
    edge1 = UndirectedGraph.Edge(node_map[1], node_map[2])
    edge2 = UndirectedGraph.Edge(node_map[1], node_map[3])
    edge3 = UndirectedGraph.Edge(node_map[2], node_map[4])
    edge4 = UndirectedGraph.Edge(node_map[0], node_map[1])
    edge5 = UndirectedGraph.Edge(node_map[5], node_map[6])
    # Build up the graph.
    graph = UndirectedGraph()
    graph.add_nodes(node_map.values())
    graph.add_edges([edge1, edge2, edge3, edge4, edge5])

    print("The graph is disjoint? " + str(disjoint(graph)))
