import json
from pathlib import Path

from app.algorithms.graph import Graph
from app.models.location import Location


class GraphLoader:

    @staticmethod
    def load():

        graph = Graph()

        locations = {}

        json_path = (
            Path(__file__)
            .parent
            / "city_graph.json"
        )

        with open(json_path, "r") as file:

            data = json.load(file)

        for location in data["locations"]:

            locations[location["id"]] = Location(

                location["id"],
                location["name"],
                location["latitude"],
                location["longitude"]

            )

        for road in data["roads"]:

            graph.add_edge(

                road["source"],
                road["destination"],

                distance=road["distance"],
                risk=road["risk"],
                travel_time=road["travel_time"]

            )

        return graph, locations