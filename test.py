from KB.manager import getRules, getFacts, getContraryPairs, getAssumption
from pyswip import Prolog
from abaFramework import ABAFramework
from anytree import Node, RenderTree

prolog = Prolog()
# prolog.consult("./KB/Resources/assumptions.pl")
prolog.consult("./KB/Resources/example1/assumptions.pl")
assumptions = getAssumption(prolog, "ex1Assumptions")

prolog.consult("./KB/Resources/example1/rules.pl")

rules = getRules(prolog, "ex1rules")
facts = getFacts(prolog, "ex1rules")

rules.update(facts)


prolog.consult("./KB/Resources/example1/contraries.pl")
contrariesList = getFacts(prolog, "ex1Contraries")

contraries = getContraryPairs(prolog, contrariesList)

aba1 = ABAFramework(rules, assumptions, contraries)
