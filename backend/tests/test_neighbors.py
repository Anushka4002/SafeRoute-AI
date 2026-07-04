from app.algorithms.graph import Graph

graph = Graph()

graph.add_edge("College", "Mall", 3)
graph.add_edge("College", "Library", 2)
graph.add_edge("Mall", "Hospital", 4)

print(graph.get_neighbors("College"))