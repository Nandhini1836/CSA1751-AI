bird(sparrow).
bird(penguin).

can_fly(sparrow).
cannot_fly(penguin).

flies(X) :- can_fly(X).
flies(X) :- bird(X), \+ cannot_fly(X).
