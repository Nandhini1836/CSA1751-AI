def minimax(depth, index, is_max, values, max_depth):
    # Base case: leaf node
    if depth == max_depth:
        return values[index]

    if is_max:
        return max(
            minimax(depth + 1, index * 2, False, values, max_depth),
            minimax(depth + 1, index * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, values, max_depth),
            minimax(depth + 1, index * 2 + 1, True, values, max_depth)
        )


# Leaf node values (left to right)
values = [3, 5, 2, 9]

max_depth = 2   # height of the tree
result = minimax(0, 0, True, values, max_depth)

print("Optimal Value:", result)
