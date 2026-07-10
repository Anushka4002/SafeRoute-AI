from app.algorithms.priority_queue import PriorityQueue


RISK_WEIGHT = 400


def safest_path(graph, start, destination):

    distances = {}
    previous = {}

    for node in graph.graph:
        distances[node] = float("inf")
        previous[node] = None

    distances[start] = 0

    pq = PriorityQueue()
    pq.push(0, start)

    while not pq.is_empty():

        current_cost, current_node = pq.pop()

        if current_node == destination:
            break

        for neighbor, road_data in graph.neighbors(current_node).items():

            distance = road_data["distance"]
            risk = road_data["risk"]

            weight = distance + (risk * RISK_WEIGHT)

            new_cost = current_cost + weight

            if new_cost < distances[neighbor]:

                distances[neighbor] = new_cost
                previous[neighbor] = current_node

                pq.push(new_cost, neighbor)

    path = []

    node = destination

    while node is not None:

        path.append(node)
        node = previous[node]

    path.reverse()

    return path, distances[destination]