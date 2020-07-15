from enum import Enum

class Rule:
    class Type(Enum):
        RULE = "rule"
        FACT = "fact"
    
    def __init__(self, head:str, body=None):

        if not body:
            self.type = Rule.Type.FACT
            self.head = head
            self.body = set()
            self.body.add(True)

        else:
            self.type = Rule.Type.RULE
            self.head = head
            self.body = body

    def getHead(self) -> str:
        return self.head
        
    def getBody(self) -> {str}:
        return self.Body

    def get(self):
        return {'head': self.head, 'body': self.body}
        