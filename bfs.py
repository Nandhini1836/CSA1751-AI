from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


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

print("BFS Example 1:")
bfs(graph_1, 'A')
print("\n")

# ---------------- EXAMPLE 2: Small Number Tree ----------------
graph_2 = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

print("BFS Example 2:")
bfs(graph_2, 1)
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

print("BFS Example 3:")
bfs(graph_3, 1)
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

print("BFS Example 4:")
bfs(graph_4, 0)
print()
