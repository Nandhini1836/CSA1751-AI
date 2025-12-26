import heapq

def UCS_Sum1():
    graph = {
        'S': [('A', 1), ('G', 12)],
        'A': [('B', 3), ('C', 1)],
        'B': [('D', 3)],
        'C': [('D', 1), ('G', 2)],
        'D': [('G', 3)],
        'G': []
    }

    start = 'S'
    goal = 'G'

    pq = [(0, start)]
    cost_so_far = {'S': 0}
    parent = {'S': None}

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            break

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    # Path reconstruction
    path = []
    n = goal
    while n:
        path.append(n)
        n = parent[n]
    path.reverse()

    print("Path:", path)
    print("Total Cost:", cost_so_far[goal])


UCS_Sum1()
