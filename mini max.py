# ---------------------------------------
# MINIMAX ALGORITHM
# ---------------------------------------

def minimax(depth, node_index, is_maximizing, values, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        best = -float('inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, max_depth)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, max_depth)
            best = min(best, val)
        return best

# ---------------------------------------
# EXAMPLE TREE (LEAF VALUES)
# ---------------------------------------
# Leaf node values (left to right)
values = [2, 3, 5, 9, 0, 1, 7, 5]

max_depth = 3  # depth of tree

result = minimax(0, 0, True, values, max_depth)

print("Optimal value using Minimax:", result)

