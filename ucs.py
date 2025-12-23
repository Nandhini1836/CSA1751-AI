import heapq

def uniform_cost_search(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start, [start]))

    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current == goal:
            print("Path found:", " -> ".join(path))
            print("Total cost:", cost)
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )

    print("No path found")


# -------- GRAPH --------
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# -------- FUNCTION CALL (THIS IS REQUIRED) --------
uniform_cost_search(graph, 'A', 'D')
