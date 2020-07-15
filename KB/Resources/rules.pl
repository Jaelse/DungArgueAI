:- module(mod1, [bird/1, fly/1, not_fly/1]).

bird(tweety) :- penguine(tweety).
bird(bob) :- sparrow(bob).
fly(tweety) :-  bird(tweety(a,b)), not(not_fly(tweety)).
fly(bob) :- bird(bob), not(not_fly(bob)).
not_fly(tweety) :-  penguine(tweety).
not_fly(bob) :- penguine(bob).