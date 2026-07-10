from app.services.coordinate_service import CoordinateService


class MapService:

    def __init__(self, locations):

        self.coordinate_service = CoordinateService(locations)

    def build_route_response(

        self,
        algorithm,
        path,
        distance,
        risk,
        safety

    ):

        coordinates = self.coordinate_service.get_coordinates(path)

        names = []

        for coordinate in coordinates:

            names.append(coordinate["name"])

        return {

            "algorithm": algorithm,

            "path": names,

            "coordinates": coordinates,

            "distance": distance,

            "risk": risk,

            "safety_percentage": safety

        }