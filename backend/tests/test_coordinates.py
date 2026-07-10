from app.data.city_graph import locations
from app.services.coordinate_service import CoordinateService


print("\n===== Coordinate Service Test =====\n")

service = CoordinateService(locations)

path = [1, 3, 4, 5]

coordinates = service.get_coordinates(path)

for coordinate in coordinates:
    print(coordinate)