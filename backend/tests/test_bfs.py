from app.algorithms.graph import Graph
from app.algorithms.bfs import bfs

graph = Graph()

graph.add_edge("College", "Mall", 3)
graph.add_edge("College", "Library", 2)
graph.add_edge("Mall", "Hospital", 4)
graph.add_edge("Library", "Hospital", 5)
graph.add_edge("Hospital", "Police Station", 1)

print("\nBFS Traversal\n")

result = bfs(graph, "College")

print(result)