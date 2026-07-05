from app.algorithms.graph import Graph
from app.algorithms.dijkstra import shortest_path


graph = Graph()

graph.add_edge("College", "Mall", 3)
graph.add_edge("College", "Library", 2)
graph.add_edge("Mall", "Hospital", 4)
graph.add_edge("Library", "Hospital", 5)
graph.add_edge("Hospital", "Police Station", 1)

path, distance = shortest_path(
    graph,
    "College",
    "Police Station"
)

print("\nShortest Path\n")

print(path)

print("\nTotal Distance")

print(distance)