edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(c, d, 2).

best_first(Start, Goal) :-
    edge(Start, Goal, _).
