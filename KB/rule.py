from enum import Enum

class Rule:
    class Type(Enum):
        RULE = "rule"
        FACT = "fact"
        ASSUMPTION = "assumption"
    
    def __init__(self, head:str, body=None, assumption:bool=False):

        if not body:
            if not assumption:
                self.type = Rule.Type.FACT
                self.head = head
                self.body = set()
                self.body.add(True)
            else:
                self.type = Rule.Type.ASSUMPTION
                self.head = head
                self.body = set()
                self.body.add("ASMP")

        else:
            self.type = Rule.Type.RULE
            self.head = head
            self.body = body

    def getHead(self) -> str:
        return self.head
        
    def getBody(self) -> {str}:
        return self.body

    def get(self):
        return {'head': self.head, 'body': self.body}
        