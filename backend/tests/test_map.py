from app.services.map_service import MapService
from app.data.city_graph import locations

service = MapService(locations)

print("\n===== Map Service Test =====\n")

result = service.build_route_response(

    algorithm="Safest Route",

    path=[1, 3, 4, 5],

    distance=600,

    risk=1.1,

    safety=63.0

)

print(result)