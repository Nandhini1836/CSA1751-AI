**ALGORITHM FOR BFS**



Represent the graph using an adjacency list

Create an empty queue Q

Create an empty set/list Visited

Add StartNode to Visited

Enqueue StartNode into Q

While Q is not empty do

Dequeue a node from Q → CurrentNode

Visit CurrentNode

For each neighbor of CurrentNode in Graph do

If neighbor is not in Visited then

Add neighbor to Visited

Enqueue neighbor into Q

End If

End For

End While

End BFS


**DFS**



Represent the graph using adjacency list

Create an empty set Visited

Define a recursive DFS function

If node is not in Visited then

→ Visit the node

→ Add node to Visited

→ For each adjacent node

  Call DFS recursively

End DFS Algorithm


**water jug**



Define the capacity of Jug1 and Jug2

Define the target amount

Create an empty queue Q

Create an empty set Visited

Insert the initial state (0,0) into Q

While Q is not empty do

→ Remove a state (x,y) from Q

→ If x or y equals target, stop

→ Generate all possible states using operations:
 Fill jug, Empty jug, Pour water

→ For each generated state

  If state is not in Visited then

  Add state to Visited

  Insert state into Q

End While

End Water Jug Algorithm


****a* arthimatic****



Represent graph with cost and heuristic values

Create an open list and closed list

Insert start node into open list

While open list is not empty do

→ Select node with lowest f(n) = g(n) + h(n)

→ If node is goal, stop

→ Move node to closed list

→ Expand neighbors

→ Update costs and parent nodes

End While

End A* Algorithm


**mini max**



Generate game tree

If terminal state reached, return score

If maximizing player then

→ Select maximum value from children

Else minimizing player

→ Select minimum value from children

Return best value

End Minimax Algorithm


**alpha beta**



Start with alpha = −∞ and beta = +∞

Apply minimax algorithm

Prune branches when beta ≤ alpha

Continue until optimal value found

Return best value

End Alpha-Beta Algorithm


**decision tree**



Collect training data

Select best attribute using information gain

Split dataset based on attribute

Repeat recursively for each subset

Stop when leaf node reached

Use tree for prediction

End Decision Tree Algorithm


**crypt arthematic**




Identify all unique letters in the problem

Assign digits (0–9) to letters

Ensure no two letters have same digit

Ensure leading letters are not zero

Form numbers using assigned digits

Check if arithmetic equation is satisfied

If satisfied, display solution

Repeat for all possible combinations

End Crypt-Arithmetic Algorithm



**8 puzzle**




Represent the puzzle as a 3×3 matrix

Define the Goal State

Create an empty queue Q

Create an empty set Visited

Insert the Initial State into Q

Add Initial State to Visited

While Q is not empty do

→ Remove the front state from Q as CurrentState

→ If CurrentState equals Goal State, stop

→ Find the position of the blank tile

→ Generate all possible moves of the blank tile

→ For each generated state

  If state is not in Visited then

  Add state to Visited

  Insert state into Q

End While

End 8-Puzzle Algorithm


**neutral network**



Initialize input values

Initialize weight values

Initialize bias value

Define the activation function (Sigmoid)

Calculate weighted sum (Net Input)

Add bias to the weighted sum

Apply activation function to the net input

Store the result as output

Display the output

End Neural Network Algorithm


**greedy bfs**


Represent the graph using an adjacency list

Define a heuristic function h(n) for each node

Create an empty priority queue Q (ordered by h(n))

Create an empty set/list Visited

Add StartNode to Visited

Insert StartNode into Q with priority h(StartNode)

While Q is not empty do

Remove the node with minimum heuristic value from Q → CurrentNode

Visit CurrentNode

If CurrentNode == GoalNode then
  Stop and return success
End If

For each neighbor of CurrentNode in Graph do

 If neighbor is not in Visited then

  Add neighbor to Visited

  Insert neighbor into Q with priority h(neighbor)

 End If

End For

End While

End Greedy Best-First Search
