hanoi(1, From, To, _) :-
    write('Move disk from '), write(From),
    write(' to '), write(To), nl.

hanoi(N, From, To, Aux) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, From, Aux, To),
    hanoi(1, From, To, Aux),
    hanoi(N1, Aux, To, From).
