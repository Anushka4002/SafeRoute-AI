from app.algorithms.dijkstra import shortest_path as dijkstra
from app.algorithms.astar import astar

from app.data.city_graph import graph, locations

print("\n===== Comparing Algorithms =====\n")

# Dijkstra
dijkstra_path, dijkstra_distance = dijkstra(
    graph,
    1,
    5
)

# A*
astar_path, astar_distance = astar(
    graph,
    locations,
    1,
    5
)

print("Dijkstra")
print("Path:")

for node in dijkstra_path:
    print(locations[node].name)

print("Distance =", dijkstra_distance)

print()

print("A*")
print("Path:")

for node in astar_path:
    print(locations[node].name)

print("Distance =", astar_distance)

print()

if dijkstra_distance == astar_distance:
    print("✅ Both algorithms found the same shortest route.")
else:
    print("❌ Algorithms returned different results.")