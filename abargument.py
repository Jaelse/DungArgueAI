from anytree import Node, RenderTree
from KB.rule import Rule

class ABArgument:
    def __init__(self, rule:Rule, **kwargs):
        self.conclusion = rule.getHead()
        self.rule = rule

        if rule.type == Rule.Type.ASSUMPTION:
            if kwargs.get('vulnerability') == None:
                raise Exception("for rule type:"+rule.type.value+" vulnerability is needed not set")    
            
            self.vulnerability = kwargs.get('vulnerability')

            self.node = Node(name=self.conclusion, parent=None, conclusion = self.conclusion, rule= rule.get(), vulnerability=self.vulnerability)
            self.subArguments = None
        elif rule.type == Rule.Type.FACT:
            self.vulnerability = kwargs.get('vulnerability')

            self.rule = rule
            self.node = Node(name=self.conclusion, parent=None,  conclusion = self.conclusion, rule = rule.get(), vulnerability= self.vulnerability)
            self.subArguments = None
        else:
            self.vulnerability = set()
            if kwargs.get('subargs') == None:
                raise Exception("for rule type:"+rule.type.value+" subargs is needed not set")

            self.subArguments = kwargs.get('subargs')

            allNodes = []
            for arg in self.subArguments:
                newChildNode = Node(name=arg.getConclusion(), conclusion= arg.getConclusion(), rule= arg.getRule().get(), vulnerability=arg.getVulnerability())
                allNodes.append(newChildNode)
                
                if arg.getVulnerability() != None:
                    self.vulnerability.update(arg.getVulnerability())

            if not self.vulnerability:
                self.vulnerability = None

            self.node = Node(name=self.conclusion, parent=None, children=allNodes,  conclusion = self.conclusion, rule = rule.get(), vulnerability=self.vulnerability)

    def setConclusionRule(self, conclusionRule:Rule):
        self.conclusionRule = conclusionRule

    def setConclusion(self, conclusion):
        self.conclusion = conclusion

    def getConclusion(self) -> str:
        return self.conclusion
    
    def getRule(self) -> Rule:
       return self.rule

    def showArgument(self):
        for pre, fill, node in RenderTree(self.getNode()):
            print("%s%s" % (pre, node.name))
    
    def getVulnerability(self):
        return self.vulnerability

    def getNode(self):
        return self.node
    