state(middle, onfloor, middle, hasnot).

move(state(middle, onfloor, middle, hasnot),
     grasp,
     state(middle, onfloor, middle, has)).

move(state(atdoor, onfloor, atwindow, hasnot),
     push,
     state(atwindow, onfloor, atwindow, hasnot)).
