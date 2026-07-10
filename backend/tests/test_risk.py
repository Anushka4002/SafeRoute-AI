from app.services.risk_service import RiskService
from app.data.city_graph import graph

risk_service = RiskService(graph)

print("\n===== Risk Service Test =====\n")

path = [1, 3, 4, 5]

print("Path:", path)

print("Total Risk:")
print(risk_service.total_risk(path))

print()

print("Average Risk:")
print(risk_service.average_risk(path))

print()

print("Safety Percentage:")
print(risk_service.safety_percentage(path))

print()

print("Risk Status:")
print(risk_service.risk_status(path))