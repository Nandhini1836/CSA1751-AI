from heapq import heappush, heappop

# ---------- Puzzle helpers ----------

GOAL = "123456780"   # 0 = blank

def to_str(board):
    return "".join(str(x) for x in board)

def print_board(state):
    s = list(state)
    print(s[0], s[1], s[2])
    print(s[3], s[4], s[5])
    print(s[6], s[7], s[8])
    print()

# ---------- Heuristics ----------

def misplaced_tiles(state):
    return sum(1 for i, v in enumerate(state)
               if v != "0" and v != GOAL[i])

def manhattan_distance(state):
    dist = 0
    for i, v in enumerate(state):
        if v == "0":
            continue
        goal_pos = GOAL.index(v)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_pos, 3)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

def heuristic(state):
    return manhattan_distance(state)

# ---------- State expansion ----------

moves = {
    0: [1,3], 1: [0,2,4], 2: [1,5],
    3: [0,4,6], 4: [1,3,5,7], 5: [2,4,8],
    6: [3,7], 7: [4,6,8], 8: [5,7]
}

def neighbors(state):
    zero = state.index("0")
    for m in moves[zero]:
        s = list(state)
        s[zero], s[m] = s[m], s[zero]
        yield to_str(s)

# ---------- A* Search ----------

def a_star(start):
    start = to_str(start)

    open_list = []
    heappush(open_list, (0, start))

    g = {start: 0}
    parent = {start: None}
    visited = set()

    while open_list:
        _, state = heappop(open_list)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in neighbors(state):
            if nxt not in g or g[state] + 1 < g[nxt]:
                g[nxt] = g[state] + 1
                f = g[nxt] + heuristic(nxt)
                parent[nxt] = state
                heappush(open_list, (f, nxt))

    return None

# ---------- Run Example (SOLVABLE) ----------

start_state = [
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
]

path = a_star(start_state)

if path is None:
    print("No solution exists for this puzzle.")
else:
    print("Steps =", len(path) - 1)
    print("\nSolution Path:\n")
    for s in path:
        print_board(s)
