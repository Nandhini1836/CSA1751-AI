goal(c).

rule(c) :- a, b.
a.
b.

backward(X) :- goal(X).
