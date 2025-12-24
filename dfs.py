# DFS FUNCTION (Recursive)
def dfs(graph, start):
    visited = set()
    result = []

    def dfs_visit(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                dfs_visit(neighbor)

    dfs_visit(start)
    return result


# ---------------- EXAMPLE 1 ----------------
graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("Example 1 DFS:", dfs(graph1, 'A'))


# ---------------- EXAMPLE 2 ----------------
graph2 = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

print("Example 2 DFS:", dfs(graph2, 1))


# ---------------- EXAMPLE 3 ----------------
graph3 = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: []
}

print("Example 3 DFS:", dfs(graph3, 1))


# ---------------- EXAMPLE 4 ----------------
graph4 = {
    'X': ['Y', 'Z'],
    'Y': ['P', 'Q'],
    'Z': ['R'],
    'P': [],
    'Q': [],
    'R': []
}

print("Example 4 DFS:", dfs(graph4, 'X'))
