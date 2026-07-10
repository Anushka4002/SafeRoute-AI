from app.data.city_graph import graph, locations
from app.services.route_service import RouteService

service = RouteService(graph, locations)

print("\n===== Safest Route Test =====\n")

result = service.get_safest_route(
    1,
    5
)

print("Algorithm:")
print(result["algorithm"])

print("\nPath:")

for node in result["path"]:
    print(node)

print("\nCoordinates:")

for coordinate in result["coordinates"]:
    print(coordinate)

print("\nDistance:")
print(result["distance"], "meters")

print("\nRisk:")
print(result["risk"])

print("\nSafety Percentage:")
print(result["safety_percentage"], "%")