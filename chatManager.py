import openai

import json
import historyManager
import chatFunction
import values

openai.api_key = json.loads(open("./config.json", "r").read())["api_key"]
    
def userInput(myChat):
    user_input = input("You: ")
    match user_input.lower():
        case "exit"|"quit"|"bye":
            historyManager.dumpHistory(myChat)
            print("ChatGPT: Goodbye!")
            return values.BYE
        case "\t":
            return chatFunction.redirect(myChat)
        case _:
            myChat.addUserMessage(user_input)
            myChat.history.append({"role": "user", "content": user_input})
            return values.INPUT
        
def GPTResponse(myChat):
    response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = myChat.history,
            max_tokens = 1024,
            temperature = 0.6
        ) 
    myChat.addGPTMessage(response.choices[0].message.content)
    myChat.history.append({"role": "assistant", "content": response.choices[0].message.content})
