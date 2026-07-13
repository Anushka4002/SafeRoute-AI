from app.services.coordinate_service import CoordinateService
from app.services.osm_service import OSMService


class MapService:

    def __init__(self, locations):
        self.coordinate_service = CoordinateService(locations)
        self.osm_service = OSMService()

    def build_route_response(
        self,
        algorithm,
        path,
        distance,
        risk,
        safety,
        travel_time=None,
        warnings=None
    ):

        coordinates = self.coordinate_service.get_coordinates(path)

        names = []
        for coordinate in coordinates:
            names.append(coordinate["name"])

        osm_url = self.osm_service.build_osm_url(coordinates)
        google_maps_url = self.osm_service.build_google_maps_url(coordinates)
        route_summary = self.osm_service.build_route_summary(coordinates)

        return {
            "algorithm": algorithm,
            "path": names,
            "coordinates": coordinates,
            "route_summary": route_summary,
            "osm_url": osm_url,
            "google_maps_url": google_maps_url,
            "distance": distance,
            "risk": risk,
            "safety_percentage": safety,
            "travel_time": travel_time,
            "warnings": warnings if warnings is not None else []
        }