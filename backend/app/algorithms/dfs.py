def dfs(graph, start):
    """
    Perform Depth First Search.

    Parameters:
        graph : Graph object
        start : Starting node

    Returns:
        List containing DFS traversal.
    """

    visited = set()
    traversal = []

    def dfs_visit(node):
        visited.add(node)
        traversal.append(node)

        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)

    return traversal