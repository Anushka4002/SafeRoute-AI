from app.algorithms.dijkstra import shortest_path
from app.data.city_graph import graph
from app.data.city_graph import locations


print("\n===== Dijkstra Test =====\n")

path, distance = shortest_path(
    graph,
    1,
    5
)

print("Path:")

for node in path:
    print(locations[node].name)

print(f"\nTotal Distance: {distance} meters")