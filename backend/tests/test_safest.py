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

print("\nDistance:")
print(result["distance"], "meters")

print("\nRisk Score:")
print(result["risk_score"])

print("\nSafety Percentage:")
print(result["safety_percentage"], "%")

print("\nStatus:")
print(result["status"])

print("\nCost:")
print(result["cost"])