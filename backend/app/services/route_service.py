from app.algorithms.dijkstra import shortest_path as dijkstra
from app.algorithms.astar import shortest_path as astar


class RouteService:

    def __init__(self, graph, locations):
        self.graph = graph
        self.locations = locations

    def shortest_route(self, source, destination):
        """
        Uses Dijkstra Algorithm
        """
        return dijkstra(
            self.graph,
            source,
            destination
        )

    def fastest_route(self, source, destination):
        """
        Future implementation:
        Uses travel_time instead of distance.
        """
        return dijkstra(
            self.graph,
            source,
            destination
        )

    def safest_route(self, source, destination):
        """
        Future implementation:
        Uses risk score.
        """
        return dijkstra(
            self.graph,
            source,
            destination
        )

    def smart_route(self, source, destination):
        """
        Uses A* Search.
        """
        return astar(
            self.graph,
            self.locations,
            source,
            destination
        )