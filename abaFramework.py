from KB.rule import Rule
from pyswip import Prolog
from anytree import Node, RenderTree
from abargument import ABArgument

class ABAFramework:
    def __init__(self, rules:Rule, assumptions:Rule, contraries:Rule):
        self.rules = rules
        self.assumptions = assumptions
        self.contraries = contraries
        self.language = set()
        self.setLanguage()
        self.arguments = set()
        self.setArguments()
        self.attacks = set()
        self.setAttacks()

    def setLanguage(self):
        for rule in self.rules:
            if rule.type == "fact":
                self.language.add(rule.head)
            else:
                self.language.add(rule.head)
                for predicate in rule.body:
                    self.language.add(predicate)
    
    def getContrary(self, word):
        for a,b in self.contraries:
            if a == word:
                return b
            elif b == word:
                return a
            else:
                return None
    
    def setArguments(self):
        assUFacts = set()

        # Making arguments from all the assumptions
        for ass in list(self.assumptions):
            vulnerability = set()
            vulnerability.add(self.getContrary(ass.getHead()))
            assUFacts.add(ass)
            self.arguments.add(ABArgument(ass, vulnerability=vulnerability))

        # Making arguments from all the facts
        for rule in list(self.rules):
            if rule.type == Rule.Type.FACT:
                assUFacts.add(rule)
                self.arguments.add(ABArgument(rule))

        
        # Making arguments from all the rules
        conclusions = set()
        for args in self.arguments:
            conclusions.add(args.getConclusion())

        ruleToMakeArgument = list(self.rules)
        while ruleToMakeArgument:
            for rule in ruleToMakeArgument:
                if rule.type == Rule.Type.RULE:
                    body = rule.getBody()
                    if body.issubset(conclusions):
                        # get the argument 
                        gettingArgs = []
                        for args in self.arguments:
                            if args.getConclusion() in body:
                                gettingArgs.append(args)
                        # make argument for this rule
                        newArg = ABArgument(rule=rule,subargs=gettingArgs)
                        # put the conclusion in the conclussion set
                        conclusions.add(newArg.getConclusion())
                        # remove the rule from ruleTOMakeArgument
                        ruleToMakeArgument.remove(newArg.getRule())
                        # ruleToMakeArgument.remove(rule)
                        self.arguments.add(newArg)
                        break
                else:
                    ruleToMakeArgument.remove(rule)
        return
    
    def showArguments(self):
        for arg in self.arguments:
            for pre, fill, node in RenderTree(arg.getNode()):
                print("%s%s" % (pre, node.conclusion))

    def setAttacks(self):
        for argA in self.arguments:
            for argB in self.arguments:
                if argB.getVulnerability() != None and argB.getConclusion() != argA.getConclusion():
                    conclusionOfA = argA.getConclusion()
                    vulnerabilitiesOfB = argB.getVulnerability() 

                    for vulnerability in list(vulnerabilitiesOfB):
                        if vulnerability == conclusionOfA:
                            self.attacks.add((argA, argB))
        
        