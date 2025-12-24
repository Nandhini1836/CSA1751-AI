def dfs(graph, start):
    visited = set()

    def dfs_visit(node):
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)


# ---------------- EXAMPLE 1: Alphabet Tree ----------------
graph_1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print("DFS Example 1:")
dfs(graph_1, 'A')
print("\n")

# ---------------- EXAMPLE 2: Small Number Tree ----------------
graph_2 = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

print("DFS Example 2:")
dfs(graph_2, 1)
print("\n")

# ---------------- EXAMPLE 3: Large Tree (1–10) ----------------
graph_3 = {
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

print("DFS Example 3:")
dfs(graph_3, 1)
print("\n")

# ---------------- EXAMPLE 4: Directed Graph ----------------
graph_4 = {
    0: [1],
    1: [3],
    2: [0],
    3: [4],
    4: [5],
    5: [7],
    6: [],
    7: [6]
}

print("DFS Example 4:")
dfs(graph_4, 0)
print()
