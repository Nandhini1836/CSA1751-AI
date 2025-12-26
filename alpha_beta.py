import math

# Tree structure
# Leaf node values
leaves = {
    'D': 2, 'E': 3,  # under B
    'F': 0, 'G': 1,  # under C left
    'H': 7, 'I': 5   # under C right (G's children)
}

# Graph connections
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [],
    'F': [], 'G': ['H', 'I'],
    'H': [], 'I': []
}

def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    # If leaf node, return its value
    if not graph[node]:
        return leaves[node]

    if maximizingPlayer:
        maxEval = -math.inf
        for child in graph[node]:
            eval = alpha_beta(child, depth+1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return maxEval
    else:
        minEval = math.inf
        for child in graph[node]:
            eval = alpha_beta(child, depth+1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return minEval

best_value = alpha_beta('A', 0, -math.inf, math.inf, True)
print("Optimal value at root (A):", best_value)
