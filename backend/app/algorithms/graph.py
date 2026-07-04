class Graph:
    """
    Graph represented using an adjacency list.

    Example:
        College ---- Mall
            |
          Library
    """

    def __init__(self):
        # Dictionary to store graph
        self.graph = {}

    def add_node(self, node):
        """
        Add a node if it doesn't already exist.
        """
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, source, destination, weight=1):
        """
        Add an undirected weighted edge.
        """

        self.add_node(source)
        self.add_node(destination)

        self.graph[source][destination] = weight
        self.graph[destination][source] = weight

    def get_neighbors(self, node):
        """
        Return neighbors of a node.
        """
        return self.graph.get(node, {})

    def display(self):
        """
        Display graph.
        """
        print("\nGraph Representation\n")

        for node in self.graph:
            print(f"{node}")

            for neighbor, weight in self.graph[node].items():
                print(f"   --> {neighbor} (distance = {weight})")

            print()

    def get_graph(self):
        return self.graph