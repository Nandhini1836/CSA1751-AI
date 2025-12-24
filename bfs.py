from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])

    return result


# -------- Example 1: Alphabet Tree --------
graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("Example 1 BFS:", bfs(graph1, 'A'))


# -------- Example 2: Numeric Tree --------
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

print("Example 2 BFS:", bfs(graph2, 1))


# -------- Example 3: Linear Graph --------
graph3 = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: []
}

print("Example 3 BFS:", bfs(graph3, 1))


# -------- Example 4: Multiple Branches --------
graph4 = {
    'X': ['Y', 'Z'],
    'Y': ['P', 'Q'],
    'Z': ['R'],
    'P': [],
    'Q': [],
    'R': []
}

print("Example 4 BFS:", bfs(graph4, 'X'))
