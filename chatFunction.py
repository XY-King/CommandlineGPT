import os

import chat
from chatNode import ChatNode
import values

def redirect(myChat):
    os.system('cls')
    myChat.printHistoryWithIndex()
    print("\033[92m" + "Please enter the index of the message you want to redirect: ")
    print("\033[0m")
    while True:
        index = input()
        try:
            myChat.printNodePaths(index)
            break
        except:
            print("\033[91m" + "Invalid index!" + "\033[0m")        
    redirectNode = chat.getAheadNode(myChat.chatHead, int(index))
    print("\033[92m" + "Please enter the path you want to redirect to: ")
    print("\033[0m")
    while True:
        path = input()
        if path == '\t' or (path.isdigit() and int(path) < len(redirectNode.next) and int(path) >= 0):
            break    

    # if the user wants to add a new message
    if path == "\t":
        newMessage = input("New message: ")
        # append the new message and change the path
        if redirectNode.content["role"] == "assistant":
            redirectNode.next.append(ChatNode({"role": "user", "content": newMessage}))
        elif redirectNode.content["role"] == "user":
            redirectNode.next.append(ChatNode({"role": "assistant", "content": newMessage}))
        redirectNode.path = len(redirectNode.next) - 1
        # refresh the chatEnd and the history
        myChat.refreshEnd()
        myChat.refreshHistory()
        return values.REDIRECT_NEW
    # if the user wants to redirect to an existing message
    else:
        chat.getAheadNode(myChat.chatHead, int(index)).path = int(path)
        # refresh the chatEnd and the history
        myChat.refreshEnd()
        myChat.refreshHistory()
        return values.REDIRECT
    
def generateAgain(myChat):
    if myChat.chatEnd.content["role"] != "assistant":
        print("\033[91m" + "You can only generate again for the assistant's message!" + "\033[0m")
        return values.GENERATE_AGAIN_ERROR
    return values.GENERATE_AGAIN





