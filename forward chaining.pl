fact(a).
fact(b).

rule(c) :- fact(a), fact(b).

forward(X) :- rule(X).
