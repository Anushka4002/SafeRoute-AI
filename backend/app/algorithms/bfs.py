from collections import deque


def bfs(graph, start):

    visited = set()
    order = []

    queue = deque([start])
    visited.add(start)

    while queue:

        current = queue.popleft()
        order.append(current)

        for neighbor in graph.neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return order