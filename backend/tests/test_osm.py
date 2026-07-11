from app.services.coordinate_service import CoordinateService
from app.services.osm_service import OSMService

from app.data.city_graph import locations


coordinate_service = CoordinateService(locations)

osm_service = OSMService()

path = [1, 3, 4, 5]

coordinates = coordinate_service.get_coordinates(path)

print("\n===== OSM Service Test =====\n")

print("Route Summary:\n")

print(

    osm_service.build_route_summary(

        coordinates

    )

)

print("\nOpenStreetMap URL:\n")

print(

    osm_service.build_osm_url(

        coordinates

    )

)

print("\nGoogle Maps URL:\n")

print(

    osm_service.build_google_maps_url(

        coordinates

    )

)