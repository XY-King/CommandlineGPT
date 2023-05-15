from chatNode import ChatNode
import time
import json
import prompts

class Chat:
    def __init__(self):
        chatHead = ChatNode(prompts.systemMessage)
        self.chatHead = chatHead
        self.chatEnd = chatHead

        self.title = ""
        self.history = []
    
    def refreshEnd(self):
        nowNode = self.chatHead
        while True:
            if nowNode.path >= len(nowNode.next):
                break
            nowNode = nowNode.next[nowNode.path]
            if nowNode.next == []:
                break
        self.chatEnd = nowNode

    def addUserMessage(self, user_input):
        input = {"role": "user", "content": user_input}
        self.chatEnd.addNext(ChatNode(input))
        self.chatEnd = self.chatEnd.next[0]
    
    def addGPTMessage(self, GPTMessage):
        message = {"role": "assistant", "content": GPTMessage}
        if self.chatEnd.content["role"] != "assistant":
            self.chatEnd.addNext(ChatNode(message))
            self.chatEnd = self.chatEnd.next[0]
        else:
            previousNode = getAheadNode(self.chatHead, self.chatEnd)
            previousNode.addNext(ChatNode(message))
            previousNode.path = len(previousNode.next) - 1
            self.chatEnd = previousNode.next[previousNode.path]

    
    def printHistory(self):
        nowNode = self.chatHead
        while True:
            if nowNode.content["role"] == "user":
                print("\033[1;31mYou: " + nowNode.content["content"])
                print("\033[0m")
            elif nowNode.content["role"] == "assistant":
                print("ChatGPT: " + nowNode.content["content"])
            if nowNode.next == []:
                return
            nowNode = nowNode.next[nowNode.path]
    
    def printHistoryWithIndex(self):
        index = 0
        nowNode = self.chatHead
        while True:
            indexPrint = "(" + str(index) + ") "
            if nowNode.content["role"] == "user":
                print(indexPrint + "\033[1;31m" + "You: " + nowNode.content["content"])
                print("\033[0m")
                index += 1
            elif nowNode.content["role"] == "assistant":
                print(indexPrint + "ChatGPT: " + nowNode.content["content"])
                index += 1
            if nowNode.next == []:
                return
            nowNode = nowNode.next[nowNode.path]

    def printNodePaths(self, index):
        nowNode = getAheadNodeWithTimes(self.chatHead, int(index))
        for i in range(len(nowNode.next)):
            print(str(i) + ":", end=" ")
            print(nowNode.next[i].content)
            print()

    def dumpHistory(self):
        # dump all the history to a list
        historyList = treeToDict(self.chatHead)
        # make the title for the json file
        localtime = time.localtime(time.time())
        self.title = "./history/"
        for i in range(5):
            self.title += str(localtime[i])
            self.title += "_"
        self.title += ".json"
        # write the history to the json file
        with open(self.title, "w") as f:
            f.write(json.dumps(historyList))

    def refreshHistory(self):
        nowNode = self.chatHead
        self.history = []
        while True:
            self.history.append(nowNode.content)
            if nowNode.path >= len(nowNode.next):
                break
            nowNode = nowNode.next[nowNode.path]
            if nowNode.next == []:
                self.history.append(nowNode.content)
                break

def treeToDict(node):
    if node == None:
        return None
    result = {
        "value": node.content,
        "path": node.path,
        "children": [treeToDict(child) for child in node.next]
    }
    return result
        
def dictToTree(myList):
    if myList == {}:
        return None
    result = ChatNode(myList["value"])
    result.path = myList["path"]
    result.next = [dictToTree(child) for child in myList["children"]]
    return result

def getAheadNodeWithTimes(head, index):
    nowNode = head
    for i in range(index):
        nowNode = nowNode.next[nowNode.path]
    return nowNode

def getAheadNode(head, node):
    nowNode = head
    while True:
        if nowNode.next == []:
            return None
        if nowNode.next[nowNode.path] == node:
            return nowNode
        nowNode = nowNode.next[nowNode.path]




