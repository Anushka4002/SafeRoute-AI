def dfs(graph, start):

    visited = set()
    order = []

    def dfs_visit(node):

        visited.add(node)
        order.append(node)

        for neighbor in graph.neighbors(node):

            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)

    return order