from app.algorithms.astar import astar
from app.data.city_graph import graph, locations

print("\n===== A* Search Test =====\n")

path, distance = astar(
    graph,
    locations,
    1,
    5
)

print("Path:")

for node in path:
    print(locations[node].name)

print(f"\nTotal Distance: {distance} meters")