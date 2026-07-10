class CoordinateService:

    def __init__(self, locations):

        self.locations = locations

    def get_coordinates(self, path):

        coordinates = []

        for node in path:

            location = self.locations[node]

            coordinates.append({

                "id": location.id,
                "name": location.name,
                "latitude": location.latitude,
                "longitude": location.longitude

            })

        return coordinates