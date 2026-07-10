from app.algorithms.dijkstra import shortest_path
from app.algorithms.astar import astar
from app.algorithms.safest_path import safest_path
from app.services.risk_service import RiskService


class RouteService:

    def __init__(self, graph, locations):

        self.graph = graph
        self.locations = locations
        self.risk_service = RiskService(graph)

    def _convert_names(self, path):

        return [self.locations[node].name for node in path]

    def get_dijkstra_route(self, source, destination):

        path, distance = shortest_path(
            self.graph,
            source,
            destination
        )

        return {
            "algorithm": "Dijkstra",
            "path": self._convert_names(path),
            "distance": distance
        }

    def get_astar_route(self, source, destination):

        path, distance = astar(
            self.graph,
            self.locations,
            source,
            destination
        )

        return {
            "algorithm": "A*",
            "path": self._convert_names(path),
            "distance": distance
        }

    def get_safest_route(self, source, destination):

        path, cost = safest_path(
            self.graph,
            source,
            destination
        )

        total_distance = 0

        for i in range(len(path) - 1):

            road = self.graph.neighbors(path[i])[path[i + 1]]
            total_distance += road["distance"]

        return {

            "algorithm": "Safest Route",

            "path": self._convert_names(path),

            "distance": total_distance,

            "risk_score":
                self.risk_service.average_risk(path),

            "safety_percentage":
                self.risk_service.safety_percentage(path),

            "status":
                self.risk_service.risk_status(path),

            "cost":
                round(cost, 2)

        }