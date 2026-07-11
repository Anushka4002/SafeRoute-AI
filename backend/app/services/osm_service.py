from urllib.parse import quote


class OSMService:

    def build_osm_url(self, coordinates):

        if not coordinates:
            return ""

        latitude = coordinates[0]["latitude"]
        longitude = coordinates[0]["longitude"]

        return (
            f"https://www.openstreetmap.org/"
            f"?mlat={latitude}&mlon={longitude}"
            f"#map=15/{latitude}/{longitude}"
        )

    def build_google_maps_url(self, coordinates):

        if not coordinates:
            return ""

        points = []

        for coordinate in coordinates:

            points.append(

                f'{coordinate["latitude"]},{coordinate["longitude"]}'

            )

        route = "/".join(points)

        route = quote(route)

        return (

            "https://www.google.com/maps/dir/"

            + route

        )

    def build_route_summary(self, coordinates):

        summary = []

        for coordinate in coordinates:

            summary.append(

                coordinate["name"]

            )

        return " → ".join(summary)