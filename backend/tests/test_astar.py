from app.algorithms.astar import shortest_path
from app.data.city_graph import graph
from app.data.city_graph import locations


print("\n===== A* Search Test =====\n")

path, distance = shortest_path(
    graph,
    locations,
    1,
    5
)

print("Path:")

for node in path:
    print(locations[node].name)

print(f"\nTotal Distance: {distance} meters")