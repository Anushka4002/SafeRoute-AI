from app.data.graph_loader import GraphLoader

graph, locations = GraphLoader.load()

print("\n===== Graph Loader Test =====\n")

print("Locations Loaded:")

for location in locations.values():
    print(location)

print("\nGraph:\n")

print(graph)