from app.data.city_graph import graph, locations

print("\n===== Locations =====\n")

for location in locations.values():
    print(location)

print("\n===== Graph =====\n")

graph.display()