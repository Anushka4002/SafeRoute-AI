from app.algorithms.dfs import dfs
from app.data.city_graph import graph, locations

print("\nDFS Traversal\n")

result = dfs(graph, 1)

for node in result:
    print(locations[node].name)