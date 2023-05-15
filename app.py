import os

import chat
import chatManager
import historyManager
import values

def main():
    os.system('cls')
    print("Welcome to AusunGPT!")
    myChat = chat.Chat()
    # if the history folder is not empty, ask the user to choose a history
    if os.listdir("./history") != []:
        historyManager.chooseHistory(myChat)
    while True:
        os.system('cls')
        myChat.printHistory()
        match chatManager.userInput(myChat):
            case values.BYE:
                historyManager.dumpHistory(myChat)
                break
            case values.INPUT|values.REDIRECT_NEW:
                chatManager.GPTResponse(myChat)
            case values.REDIRECT:
                pass
            case values.GENERATE_AGAIN:
                chatManager.GPTResponse(myChat)

if __name__ == '__main__':
    main()