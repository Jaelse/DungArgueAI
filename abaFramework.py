from KB.rule import Rule
from pyswip import Prolog

class ABAFramework:
    def __init__(self, rules:Rule, assumptions:Rule, contraries:Rule):
        self.rules = rules
        self.assumptions = assumptions
        self.contraries = contraries
        self.language = set()
        self.setLanguage()

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
        return
