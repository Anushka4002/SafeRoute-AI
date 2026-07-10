from app.algorithms.dijkstra import shortest_path
from app.algorithms.astar import astar
from app.algorithms.safest_path import safest_path

from app.services.risk_service import RiskService
from app.services.map_service import MapService


class RouteService:

    def __init__(self, graph, locations):

        self.graph = graph
        self.locations = locations

        self.risk_service = RiskService(graph)
        self.map_service = MapService(locations)

    def get_dijkstra_route(self, source, destination):

        path, distance = shortest_path(
            self.graph,
            source,
            destination
        )

        risk = self.risk_service.total_risk(path)

        safety = self.risk_service.safety_percentage(path)

        return self.map_service.build_route_response(

            "Dijkstra",

            path,

            distance,

            risk,

            safety

        )

    def get_astar_route(self, source, destination):

        path, distance = astar(

            self.graph,

            self.locations,

            source,

            destination

        )

        risk = self.risk_service.total_risk(path)

        safety = self.risk_service.safety_percentage(path)

        return self.map_service.build_route_response(

            "A* Search",

            path,

            distance,

            risk,

            safety

        )

    def get_safest_route(self, source, destination):

        path, cost = safest_path(

            self.graph,

            source,

            destination

        )

        distance = 0

        for i in range(len(path) - 1):

            road = self.graph.neighbors(path[i])[path[i + 1]]

            distance += road["distance"]

        risk = self.risk_service.total_risk(path)

        safety = self.risk_service.safety_percentage(path)

        return self.map_service.build_route_response(

            "Safest Route",

            path,

            distance,

            risk,

            safety

        )