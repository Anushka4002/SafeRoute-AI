from app.algorithms.dijkstra import shortest_path
from app.algorithms.astar import astar
from app.algorithms.safest_path import safest_path
from app.algorithms.fastest_path import fastest_path

from app.services.risk_service import RiskService
from app.services.map_service import MapService
from app.services.geocode_service import GeocodeService
from app.services.nearest_node_service import NearestNodeService


class RouteService:

    def __init__(self, graph, locations):

        self.graph = graph
        self.locations = locations

        self.risk_service = RiskService(graph)
        self.map_service = MapService(locations)
        self.geocode_service = GeocodeService()
        self.nearest_node_service = NearestNodeService(locations)

    def _calculate_distance(self, path):

        distance = 0
        for i in range(len(path) - 1):
            road = self.graph.neighbors(path[i])[path[i + 1]]
            distance += road["distance"]
        return distance

    def _calculate_travel_time(self, path):

        travel_time = 0
        for i in range(len(path) - 1):
            road = self.graph.neighbors(path[i])[path[i + 1]]
            travel_time += road["travel_time"]
        return travel_time

    def _generate_warnings(self, path):

        warnings = []

        avg_risk = self.risk_service.average_risk(path)
        safety = self.risk_service.safety_percentage(path)

        if safety < 50:
            warnings.append("Overall route safety is low. Consider an alternate route.")

        if avg_risk >= 0.5:
            warnings.append("This route passes through high-risk road segments.")

        return warnings

    def get_dijkstra_route(self, source, destination):

        path, distance = shortest_path(self.graph, source, destination)

        risk = self.risk_service.total_risk(path)
        safety = self.risk_service.safety_percentage(path)
        travel_time = self._calculate_travel_time(path)
        warnings = self._generate_warnings(path)

        return self.map_service.build_route_response(
            "Dijkstra", path, distance, risk, safety, travel_time, warnings
        )

    def get_astar_route(self, source, destination):

        path, distance = astar(self.graph, self.locations, source, destination)

        risk = self.risk_service.total_risk(path)
        safety = self.risk_service.safety_percentage(path)
        travel_time = self._calculate_travel_time(path)
        warnings = self._generate_warnings(path)

        return self.map_service.build_route_response(
            "A* Search", path, distance, risk, safety, travel_time, warnings
        )

    def get_fastest_route(self, source, destination):

        path, cost = fastest_path(self.graph, source, destination)

        distance = self._calculate_distance(path)
        risk = self.risk_service.total_risk(path)
        safety = self.risk_service.safety_percentage(path)
        travel_time = self._calculate_travel_time(path)
        warnings = self._generate_warnings(path)

        return self.map_service.build_route_response(
            "Fastest Route", path, distance, risk, safety, travel_time, warnings
        )

    def get_safest_route(self, source, destination):

        path, cost = safest_path(self.graph, source, destination)

        distance = self._calculate_distance(path)
        risk = self.risk_service.total_risk(path)
        safety = self.risk_service.safety_percentage(path)
        travel_time = self._calculate_travel_time(path)
        warnings = self._generate_warnings(path)

        return self.map_service.build_route_response(
            "Safest Route", path, distance, risk, safety, travel_time, warnings
        )

    def get_route_by_address(self, algorithm, source_query, destination_query):

        source_results = self.geocode_service.geocode(source_query)
        destination_results = self.geocode_service.geocode(destination_query)

        if not source_results or not destination_results:
            return {"error": "Could not find one or both addresses."}

        source_coord = source_results[0]
        destination_coord = destination_results[0]

        source_id, source_distance = self.nearest_node_service.find_nearest(
            source_coord["latitude"], source_coord["longitude"]
        )
        destination_id, destination_distance = self.nearest_node_service.find_nearest(
            destination_coord["latitude"], destination_coord["longitude"]
        )

        if algorithm == "dijkstra":
            result = self.get_dijkstra_route(source_id, destination_id)
        elif algorithm == "astar":
            result = self.get_astar_route(source_id, destination_id)
        elif algorithm == "fastest":
            result = self.get_fastest_route(source_id, destination_id)
        elif algorithm == "safest":
            result = self.get_safest_route(source_id, destination_id)
        else:
            return {"error": "Invalid algorithm"}

        result["source_matched_location"] = self.locations[source_id].name
        result["destination_matched_location"] = self.locations[destination_id].name
        result["source_snap_distance_m"] = round(source_distance, 1)
        result["destination_snap_distance_m"] = round(destination_distance, 1)

        return result