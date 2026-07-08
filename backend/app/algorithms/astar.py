from app.algorithms.priority_queue import PriorityQueue
from app.algorithms.heuristics import euclidean_distance


def shortest_path(graph, locations, start, destination):
    """
    A* Search Algorithm

    Parameters:
        graph : Graph object
        locations : Dictionary containing Location objects
        start : Starting node id
        destination : Destination node id

    Returns:
        path, total_distance
    """

    open_set = PriorityQueue()

    open_set.push(0, start)

    came_from = {}

    g_score = {}

    f_score = {}

    for node in graph.graph:

        g_score[node] = float("inf")
        f_score[node] = float("inf")

    g_score[start] = 0

    f_score[start] = euclidean_distance(
        locations[start],
        locations[destination]
    )

    while not open_set.is_empty():

        current_priority, current = open_set.pop()

        if current == destination:
            break

        for neighbor, road_data in graph.neighbors(current).items():

            distance = road_data["distance"]

            tentative_g_score = (
                g_score[current]
                +
                distance
            )

            if tentative_g_score < g_score[neighbor]:

                came_from[neighbor] = current

                g_score[neighbor] = tentative_g_score

                heuristic = euclidean_distance(
                    locations[neighbor],
                    locations[destination]
                )

                f_score[neighbor] = (
                    tentative_g_score
                    +
                    heuristic
                )

                open_set.push(
                    f_score[neighbor],
                    neighbor
                )

    path = []

    node = destination

    while node in came_from:

        path.append(node)

        node = came_from[node]

    path.append(start)

    path.reverse()

    return path, g_score[destination]