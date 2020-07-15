from KB.manager import getRules, getFacts,getContraryPairs
from pyswip import Prolog
from abaFramework import ABAFramework

prolog = Prolog()
prolog.consult("./KB/Resources/assumptions.pl")
assumptions = getFacts(prolog, "assumptions")

prolog.consult("./KB/Resources/rules.pl")

rules = getRules(prolog, "mod1")
facts = getFacts(prolog, "mod1")

rulesUFacts = rules.union(facts)

prolog.consult("./KB/Resources/contraries.pl")
contrariesList = getFacts(prolog, "contraries")

contraries = (getContraryPairs(prolog, contrariesList))

aba1 = ABAFramework(rulesUFacts, assumptions, contraries)