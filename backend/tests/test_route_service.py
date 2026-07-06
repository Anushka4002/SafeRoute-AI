from app.algorithms.graph import Graph
from app.services.route_service import RouteService

graph = Graph()

graph.add_edge("College", "Mall", 3)
graph.add_edge("College", "Library", 2)
graph.add_edge("Mall", "Hospital", 4)
graph.add_edge("Library", "Hospital", 5)
graph.add_edge("Hospital", "Police Station", 1)

service = RouteService(graph)

route = service.get_shortest_route(
    "College",
    "Police Station"
)

print("\nSafeRoute AI\n")

print("Path:")

print(route.path)

print("\nDistance:")

print(route.distance)