import heapq

# -------------------------------------------------
# A* SEARCH FUNCTION
# -------------------------------------------------
def a_star_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current in closed_set:
            continue

        closed_set.add(current)

        if current == goal:
            return g, path

        for neighbor, cost in graph[current]:
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return float("inf"), []


# =================================================
# EXAMPLE 1 (FROM YOUR FIRST IMAGE: S → G)
# =================================================
graph_1 = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4), ('D', 5)],
    'B': [('C', 4), ('E', 5)],
    'C': [],
    'D': [('E', 2)],
    'E': [('F', 4)],
    'F': [('G', 3.5)],
    'G': []
}

heuristic_1 = {
    'S': 11.5,
    'A': 10.1,
    'B': 5.8,
    'C': 3.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}

cost, path = a_star_search(graph_1, heuristic_1, 'S', 'G')
print("Example 1:")
print("Cost =", cost)
print("Path =", " -> ".join(path))
print()


# =================================================
# EXAMPLE 2 (FROM YOUR SECOND IMAGE: A → G)
# =================================================
graph_2 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('C', 2)],
    'C': [('E', 5)],
    'D': [('F', 2), ('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

heuristic_2 = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}

cost, path = a_star_search(graph_2, heuristic_2, 'A', 'G')
print("Example 2:")
print("Cost =", cost)
print("Path =", " -> ".join(path))
print()


# =================================================
# EXAMPLE 3 (SIMPLE DEMO GRAPH)
# =================================================
graph_3 = {
    'S': [('A', 2), ('B', 6)],
    'A': [('C', 2)],
    'B': [('C', 1)],
    'C': [('G', 3)],
    'G': []
}

heuristic_3 = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 1,
    'G': 0
}

cost, path = a_star_search(graph_3, heuristic_3, 'S', 'G')
print("Example 3:")
print("Cost =", cost)
print("Path =", " -> ".join(path))
