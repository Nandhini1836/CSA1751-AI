% pattern matching examples

pattern([H|_], H).          % first element
pattern([_,S|_], S).        % second element
pattern([_,_,T|_], T).      % third element

same(X, X).                 % same pattern

