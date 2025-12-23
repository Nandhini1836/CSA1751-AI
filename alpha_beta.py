def alpha_beta(depth, index, is_max, values, alpha, beta, max_depth):
    # Base condition: leaf node
    if depth == max_depth:
        return values[index]

    if is_max:
        best = -999

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                index * 2 + i,
                False,
                values,
                alpha,
                beta,
                max_depth
            )
            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                break   # Beta cut-off

        return best

    else:
        best = 999

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                index * 2 + i,
                True,
                values,
                alpha,
                beta,
                max_depth
            )
            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                break   # Alpha cut-off

        return best


# -------- LEAF NODE VALUES --------
# Game tree:
#            MAX
#         /         \
#       MIN         MIN
#     /    \       /    \
#    3      5     2      9
values = [3, 5, 2, 9]

max_depth = 2

# -------- FUNCTION CALL (THIS MAKES IT RUN) --------
result = alpha_beta(
    depth=0,
    index=0,
    is_max=True,
    values=values,
    alpha=-999,
    beta=999,
    max_depth=max_depth
)

print("Optimal Value:", result)
