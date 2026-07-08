class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(
        self,
        source,
        destination,
        distance,
        risk=0.0,
        travel_time=None,
        bidirectional=True
    ):
        self.add_node(source)
        self.add_node(destination)

        if travel_time is None:
            travel_time = distance

        self.graph[source][destination] = {
            "distance": distance,
            "risk": risk,
            "travel_time": travel_time
        }

        if bidirectional:
            self.graph[destination][source] = {
                "distance": distance,
                "risk": risk,
                "travel_time": travel_time
            }

    def neighbors(self, node):
        return self.graph.get(node, {})

    def display(self):
        print("\nGraph Representation\n")

        for node in self.graph:

            print(node)

            for neighbor, data in self.graph[node].items():

                print(
                    f"   --> {neighbor} "
                    f"(distance={data['distance']}, "
                    f"risk={data['risk']}, "
                    f"time={data['travel_time']})"
                )

            print()