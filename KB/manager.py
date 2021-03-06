from pyswip import Prolog
from KB.rule import Rule

def getFacts(prolog:Prolog, module:str):
    factsRaw = ""
    facts:Rule = set()

    for soln in prolog.query("with_output_to(atom(X), listing("+module+":_))"):
        factsRaw = soln["X"]

    factsList = factsRaw.split(".", factsRaw.count("."))

    for factRaw in factsList:

        if factRaw != "\n" and ":-" not in factRaw :
            factRaw = factRaw.replace(" ", "")
            factRaw = factRaw.replace("\n", "")

            if module == "assumptions":
                facts.add(Rule(factRaw, assumption=True))
            else:
                facts.add(Rule(factRaw)) 
            
    return facts

def getAssumption(prolog:Prolog, module:str):
    assRaw = ""

    assumption:Rule = set()

    for soln in prolog.query("with_output_to(atom(X), listing("+module+":_))"):
        assRaw = soln["X"]


    assmpList = assRaw.split(".", assRaw.count("."))
    for assRaw in assmpList:

        if assRaw != "\n" and ":-" not in assRaw :
            assRaw = assRaw.replace(" ", "")
            assRaw = assRaw.replace("\n", "")

            assumption.add(Rule(assRaw, assumption=True))
            
    return assumption


def getRules(prolog:Prolog, module:str):
    rules = set()

    rulesRaw = ""
    for soln in prolog.query("with_output_to(atom(X), listing("+module+":_))"):
        rulesRaw = soln["X"]

    rulesList = rulesRaw.split(".", rulesRaw.count("."))

    for rule in rulesList:
        head:str

        if ":-" in rule:
            r = rule.split(":-")
            headRaw = r[0]
            headRaw = headRaw.replace("\n", "")
            headRaw = headRaw.replace(" ", "")

            head = headRaw
            premises = set()
            # get the arity for all the body elements
            checkPoint = True
            print(headRaw)
            for body in prolog.query("clause("+headRaw+", B), functor(B, _, Arity)"):
                if int(body["Arity"]) == 0:
                    checkPoint = False

            if checkPoint:
                # check the body first
                # if the body elements are changing then it means 
                # there are two rule with same head
                l = ""
                for body in prolog.query("clause("+headRaw+", L), functor(L, _, Arity), arg(Pos, L, V)"):
                    if body["Arity"] > 1:
                        premises.add(body["V"])
                    else:
                        premises.add(body["L"])
                rules.add(Rule(head, premises))
            else:
                for body in prolog.query("clause("+headRaw+", L)"):
                        premises.add(body["L"])
                rules.add(Rule(head, premises))

    return rules

def getContraryPairs(prolog:Prolog, contrariesList) -> set:
    contraries = set()

    for contrary in contrariesList:
        a = None
        b = None
        for res in prolog.query("arg(Pos,"+contrary.getHead()+",Value)"):
            if res["Pos"] == 1:
                a = res["Value"]
            elif res["Pos"] == 2:
                b = res["Value"]
        contraries.add((a,b))    
    
    return contraries

#  ([a-z])\w+\([a-z,A-Z,0-9]+\) parse this to get all the atoms in the body
