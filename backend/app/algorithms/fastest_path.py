from app.algorithms.priority_queue import PriorityQueue


def fastest_path(graph, start, destination):

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

            weight = road_data["travel_time"]
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