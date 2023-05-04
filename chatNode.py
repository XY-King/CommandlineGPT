class ChatNode:
    def __init__(self, content):
        # the list of the responses
        self.next = []
        # the path of the node chosen
        self.path = 0
        # the content of the node
        self.content = content
    
    def addNext(self, nextNode):
        self.next.append(nextNode)
        if len(self.next) > 1:
            self.path = len(self.next) - 1

    def choosePath(self, path):
        self.path = path
    
