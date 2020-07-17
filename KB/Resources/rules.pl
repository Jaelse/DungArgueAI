:- module(mod1, [penguine/1, bird/1, fly/1, not_fly/1]).

penguine(tweety).
bird(tweety) :- penguine(tweety).
fly(tweety) :-  bird(tweety), not(not_fly(tweety)).
not_fly(tweety) :- penguine(tweety).