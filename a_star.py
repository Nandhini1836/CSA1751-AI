import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print("Path found:", " -> ".join(path))
            print("Total cost:", g)
            return

        closed_set.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_set:
                continue

            new_g = g + cost
            new_f = new_g + heuristic[neighbor]

            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    print("No path found")

# ✅ YOU MUST INCLUDE THIS PART — or nothing will run
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('G', 5)],
    'C': [('G', 2)],
    'D': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'G': 0
}

a_star(graph, heuristic, 'A', 'G')  # ← THIS LINE is the actual execution
