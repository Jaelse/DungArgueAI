:- module(ex1rules, [p/0, not_q/0, s/0,r/0,v/0,u/0,w/0]).

p :- q,r.
not_q :- s,v.
not_q :- t,u.
s :- t.
r.
v.
u :- w.
w.