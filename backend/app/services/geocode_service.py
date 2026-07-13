import requests


class GeocodeService:

    BASE_URL = "https://nominatim.openstreetmap.org/search"

    def geocode(self, query):

        params = {
            "q": query,
            "format": "json",
            "limit": 5
        }

        headers = {
            "User-Agent": "SafeRouteAI/1.0"
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            headers=headers,
            timeout=5
        )

        response.raise_for_status()
        results = response.json()

        suggestions = []

        for item in results:
            suggestions.append({
                "display_name": item["display_name"],
                "latitude": float(item["lat"]),
                "longitude": float(item["lon"])
            })

        return suggestions