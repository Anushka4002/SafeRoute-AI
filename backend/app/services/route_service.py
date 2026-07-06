from app.algorithms.dijkstra import shortest_path
from app.models.route import Route


class RouteService:

    def __init__(self, graph):
        self.graph = graph

    def get_shortest_route(self, start, destination):

        path, distance = shortest_path(
            self.graph,
            start,
            destination
        )

        return Route(
            path=path,
            distance=distance
        )