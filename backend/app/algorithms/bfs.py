from collections import deque


def bfs(graph, start):
    """
    Perform Breadth First Search.

    Parameters:
        graph : Graph object
        start : Starting node

    Returns:
        List containing BFS traversal.
    """

    visited = set()
    queue = deque()
    traversal = []

    visited.add(start)
    queue.append(start)

    while queue:

        current = queue.popleft()
        traversal.append(current)

        for neighbor in graph.get_neighbors(current):

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal