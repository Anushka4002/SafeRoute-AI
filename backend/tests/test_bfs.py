from app.algorithms.bfs import bfs
from app.data.city_graph import graph, locations

print("\n===== BFS Traversal =====\n")

result = bfs(graph, 1)

for node in result:
    print(locations[node].name)