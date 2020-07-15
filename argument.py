from anytree import Node, RenderTree
from KB.rule import Rule

class Argument:
    parentNode:Node
    

    def __init__(self, conclusionRule:Node):
        self.parentNode = conclusionRule

    def setConclusionRule(self, conclusionRule:Rule):
        self.conclusionRule = conclusionRule

    def setConclusion(self, conclusion):
        self.conclusion = conclusion

    def getConclusion(self) -> Rule:
        return self.conclusion

    