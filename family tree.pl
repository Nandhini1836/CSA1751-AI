parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).

male(john).
female(susan).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
