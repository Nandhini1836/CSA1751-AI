from collections import deque

# Jug capacities
CAPACITY_12 = 12
CAPACITY_8 = 8
CAPACITY_5 = 5

# Initial and goal state
initial_state = (12, 0, 0)
goal_amount = 6

# BFS function
def water_jug_bfs():
    queue = deque()
    visited = set()

    queue.append((initial_state, [initial_state]))
    visited.add(initial_state)

    while queue:
        (x, y, z), path = queue.popleft()

        # Goal condition
        if y == goal_amount:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        # All possible moves
        moves = []

        # Pour 12 -> 8
        t = min(x, CAPACITY_8 - y)
        moves.append((x - t, y + t, z))

        # Pour 12 -> 5
        t = min(x, CAPACITY_5 - z)
        moves.append((x - t, y, z + t))

        # Pour 8 -> 12
        t = min(y, CAPACITY_12 - x)
        moves.append((x + t, y - t, z))

        # Pour 8 -> 5
        t = min(y, CAPACITY_5 - z)
        moves.append((x, y - t, z + t))

        # Pour 5 -> 12
        t = min(z, CAPACITY_12 - x)
        moves.append((x + t, y, z - t))

        # Pour 5 -> 8
        t = min(z, CAPACITY_8 - y)
        moves.append((x, y + t, z - t))

        # Add valid unvisited states
        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("No solution found")

# Run the program
water_jug_bfs()




EXAMPLE 2


from collections import deque

# Jug capacities
CAPACITY_8 = 8
CAPACITY_5 = 5
CAPACITY_3 = 3

# Initial and goal state
initial_state = (8, 0, 0)
goal_state = (4, 4)

# BFS function
def water_jug_bfs():
    queue = deque()
    visited = set()

    queue.append((initial_state, [initial_state]))
    visited.add(initial_state)

    while queue:
        (x, y, z), path = queue.popleft()

        # Goal condition
        if x == goal_state[0] and y == goal_state[1]:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        moves = []

        # Pour 8 -> 5
        t = min(x, CAPACITY_5 - y)
        moves.append((x - t, y + t, z))

        # Pour 8 -> 3
        t = min(x, CAPACITY_3 - z)
        moves.append((x - t, y, z + t))

        # Pour 5 -> 8
        t = min(y, CAPACITY_8 - x)
        moves.append((x + t, y - t, z))

        # Pour 5 -> 3
        t = min(y, CAPACITY_3 - z)
        moves.append((x, y - t, z + t))

        # Pour 3 -> 8
        t = min(z, CAPACITY_8 - x)
        moves.append((x + t, y, z - t))

        # Pour 3 -> 5
        t = min(z, CAPACITY_5 - y)
        moves.append((x, y + t, z - t))

        # Add unvisited states
        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("No solution found")

# Run the program
water_jug_bfs()
