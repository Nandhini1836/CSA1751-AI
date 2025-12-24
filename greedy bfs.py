import heapq

# -------------------------------------------------
# GREEDY BEST-FIRST SEARCH FUNCTION
# -------------------------------------------------
def greedy_best_first_search(graph, heuristic, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))
    visited = set()

    while priority_queue:
        h, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )

    return []


# =================================================
# EXAMPLE 1 (FROM YOUR FIRST IMAGE: A → O)
# =================================================
graph_1 = {
    'A': ['D', 'C', 'B'],
    'D': ['F'],
    'C': ['F'],
    'B': ['E'],
    'E': ['H'],
    'H': ['G'],
    'F': ['G'],
    'G': ['O'],
    'O': []
}

heuristic_1 = {
    'A': 40,
    'D': 35,
    'C': 25,
    'B': 32,
    'E': 19,
    'H': 10,
    'F': 17,
    'G': 6,
    'O': 0
}

path1 = greedy_best_first_search(graph_1, heuristic_1, 'A', 'O')
print("Example 1 (A → O)")
print("Path:", " -> ".join(path1))
print()


# =================================================
# EXAMPLE 2 (FROM YOUR SECOND IMAGE: P → S)
# =================================================
graph_2 = {
    'P': ['R', 'C', 'A'],
    'R': ['E'],
    'C': ['R', 'U'],
    'A': ['M'],
    'M': ['L'],
    'L': ['N'],
    'U': ['S', 'N'],
    'E': ['S'],
    'N': [],
    'S': []
}

heuristic_2 = {
    'P': 10,
    'R': 4,
    'C': 6,
    'A': 11,
    'M': 9,
    'L': 9,
    'N': 6,
    'U': 4,
    'E': 3,
    'S': 0
}

path2 = greedy_best_first_search(graph_2, heuristic_2, 'P', 'S')
print("Example 2 (P → S)")
print("Path:", " -> ".join(path2))
print()


# =================================================
# EXAMPLE 3 (SIMPLE DEMO GRAPH)
# =================================================
graph_3 = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}

heuristic_3 = {
    'S': 6,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 3,
    'G': 0
}

path3 = greedy_best_first_search(graph_3, heuristic_3, 'S', 'G')
print("Example 3 (S → G)")
print("Path:", " -> ".join(path3))
