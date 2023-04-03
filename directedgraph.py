# Playing around with graphs.
import collections


class DirectedGraph:
    """The graph just contains a list of nodes and edges."""

    def __init__(self):
        self.nodes = set()
        self.edges = set()

        # The edge map is not necessary, but it's just handy.
        self.edge_map = collections.defaultdict(list)

    class Node:
        """A single node in a graph."""

        def __init__(self, value: str):
            self.value = value

        def __str__(self):
            return self.value

    class Edge:
        """A single edge in a graph."""

        def __init__(self, source: "Node", dest: "Node"):
            self.source = source
            self.dest = dest

        def __str__(self):
            return self.source + " -> " + self.value

    def add_nodes(self, node_list):
        for node in node_list:
            self.nodes.add(node)

    def add_edges(self, *edges):
        for edge in edges:
            self.edges.add(edge)
            self.edge_map[edge.source].append(edge.dest)

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


class Subgraph:
    """I could always use the DirectedGraph class for this too."""

    def __init__(self, initial_node):
        self.nodes = set()
        self.nodes.add(initial_node)

    def __str__(self):
        return ", ".join([item.value for item in self.nodes]) + "({})".format(
            hash(self)
        )

    def union(self, other_subgraph):
        self.nodes = self.nodes.union(other_subgraph.nodes)


def _print_subgraphs(subgraphs):
    for key, value in subgraphs.items():
        print("{} :: {}".format(key, value))


def disjoint(graph: DirectedGraph):
    """Determine if the given DirectedGraph is disjoint."""
    """
    This is a bit different in directed vs undirected graphs. In an
    undirected graph it's enough to just start from a single node and do a
    regular BFS. Then check at the end if visited == all nodes.
    
    In a directed graph, I don't necessarily have access to the sources of
    edges. I have two options and it depends on the type of connectedness I care
    about:
      1. If all I care about is that there is some edge between all nodes, then
         I can just ignore the edge direction and consider all edges undirected.
         But this is slow if I need to find the source of the edge and it isn't
         something I can easily look up.
      2. If I care about edge direction, start with all nodes in their own
         subgraphs. Pick a node and get all outgoing edges, and add all of 
         those nodes to the same subgraph. Keep going until all nodes have been
         checked. Then check if there are multiple subgraphs.
    """
    if not graph.nodes:
        return False

    # Initialize a list of lists with one entry for each node. That will be
    # expanded as part of the later search.
    subgraphs = {item.value: Subgraph(item) for item in graph.nodes}

    for node in graph.nodes:
        edge_destinations = graph.edge_map[node]
        for destination in edge_destinations:
            source_subgraph = subgraphs[node.value]

            # Take this destination node and find its subgraph. Then union
            # the source subgraph with the destination subgraph. Update
            # both the source and destination subgraphs to be the newly
            # unioned subgraph.
            destination_subgraph = subgraphs[destination.value]
            source_subgraph.union(destination_subgraph)
            subgraphs[node.value] = source_subgraph
            subgraphs[destination.value] = source_subgraph

            # Lastly, go through and make sure that every single node that
            # was a part of the destination subgraph is updated to the new
            # subgraph.
            for extra_node in destination_subgraph.nodes:
                subgraphs[extra_node.value] = source_subgraph

    # At this point, pick the first node in the subgraph dict and check that
    # the number of nodes == number of nodes in input graph. True iff no equal.
    return (
        True
        if len(list(subgraphs.values())[0].nodes) != len(graph.nodes)
        else False
    )


if __name__ == "__main__":
    node_map = {}
    for i in range(7):
        node_map[i] = DirectedGraph.Node(str(i))
    edge1 = DirectedGraph.Edge(node_map[1], node_map[2])
    edge2 = DirectedGraph.Edge(node_map[1], node_map[3])
    edge3 = DirectedGraph.Edge(node_map[2], node_map[4])
    edge4 = DirectedGraph.Edge(node_map[0], node_map[1])
    edge5 = DirectedGraph.Edge(node_map[5], node_map[6])
    # Build up the graph.
    graph = DirectedGraph()
    graph.add_nodes(node_map.values())
    graph.add_edges(edge1, edge2, edge3, edge4, edge5)

    # Should be True, there are two subgraphs.
    print("The graph is disjoint? " + str(disjoint(graph)))
