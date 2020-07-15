

import os
import clingo
# from rule import Rule

ctrl = clingo.Control()

# f1 = Rule(head=clingo.Function("penguine", arguments=[clingo.Function("tweety")]))

# f2 = Rule(head=clingo.Function("sparrow", arguments=[clingo.Function("bob")]))

# r1 = Rule(
#     head=clingo.Function("bird", arguments=[clingo.Function("X")]),
#     body=[clingo.Function("penguine", arguments=[clingo.Function("X")])],
# )

# r2 = Rule(
#     head=clingo.Function("bird", arguments=[clingo.Function("X")]),
#     body=[clingo.Function("sparrow", arguments=[clingo.Function("X")])],
# )

# r3 = Rule(
#     head=clingo.Function("fly", arguments=[clingo.Function("X")]),
#     body=[
#         clingo.Function(r2.head),
#         clingo.Function("not fly", arguments=[clingo.Function("X")], positive=False),
#     ],
# )

# r4 = Rule(
#     head=clingo.Function("fly", arguments=[clingo.Funcation("X")], positive=False),
#     body=[clingo.Function("penguine", arguments=[clingo.Function("X")])],
# )

# ctrl.add("base", [], f1.getRule()+f2.getRule()+r1.getRule()+r2.getRule()+r3.getRule()+r4.getRule())

# ctrl.configuration.solve.__desc_models
# ctrl.configuration.solve.models = 0
# Variable X
# sym_X = clingo.Function("X")
# # tweety
# sym_tweety = clingo.Function("tweety")
# # bob
# sym_bob= clingo.Function("bob")
# # penguine(tweety)
# sym_penguine = clingo.Function("penguine", arguments=[sym_tweety])
# # sparrow(bob)
# sym_sparrow = clingo.Function("sparrow", arguments=[sym_bob])
# # -fly(X)
# sym_fly = clingo.Function("fly", arguments=[sym_X])
# sym_penguine_X = clingo.Function("penguine", arguments=[sym_X])

# with ctrl.backend() as backend:
#     # penguine_atom = backend.add_atom(sym_penguine)
#     sparrow_atom = backend.add_atom(sym_sparrow)
#     penguine_atom = backend.add_atom(sym_penguine)
#     fly_atom = backend.add_atom(sym_fly)
#     penguine_X_atom = backend.add_atom(sym_penguine_X)

#     backend.add_rule(head = [penguine_atom])
#     backend.add_rule(head = [sparrow_atom])
#     # -fly(X) :- penguine(X)
#     backend.add_rule(head = [fly_atom], body=[penguine_X_atom])

# ctrl.add("p", ["t"], "q(t) :- a")

# ctrl.cleanup()
# cwd = os.getcwd()
# ctrl.load(cwd + "/KB/hello.lp")
ctrl.ground([("base", [])])
# for atoms in ctrl.symbolic_atoms:
#     print(atoms.symbol)
ctrl.solve(on_model=lambda m: print("Answer: {}".format(m)))
