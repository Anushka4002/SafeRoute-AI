import math


class NearestNodeService:

    def __init__(self, locations):
        self.locations = locations

    def find_nearest(self, latitude, longitude):

        nearest_id = None
        nearest_distance = float("inf")

        for loc_id, location in self.locations.items():

            distance = self._haversine(
                latitude, longitude,
                location.latitude, location.longitude
            )

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_id = loc_id

        return nearest_id, nearest_distance

    def _haversine(self, lat1, lon1, lat2, lon2):

        R = 6371000

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = (
            math.sin(dphi / 2) ** 2
            + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        )

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c