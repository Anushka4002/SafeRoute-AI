from app.algorithms.priority_queue import PriorityQueue


def shortest_path(graph, start, destination):

    distances = {}
    previous = {}

    for node in graph.graph:
        distances[node] = float("inf")
        previous[node] = None

    distances[start] = 0

    pq = PriorityQueue()
    pq.push(0, start)

    while not pq.is_empty():

        current_distance, current_node = pq.pop()

        if current_node == destination:
            break

        for neighbor, road_data in graph.neighbors(current_node).items():

            weight = road_data["distance"]

            distance = current_distance + weight
            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node

                pq.push(distance, neighbor)

    path = []

    node = destination

    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()

    return path, distances[destination]