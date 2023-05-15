## This project is a command-line wrapper for OpenAI's GPT-3.5 API. It is designed as a python practice for the author.

This project implements all the features of chat.openai.com, including chatting, preserving multiple histories, variations during the chat, and keeping a tree-structure chat history.

To build the project from source, you need to have python installed.
Then you should run the file '_init.bat'. It will create two files: 'history.json', 'config.json', and a folder named 'history'. The 'history.json' and history folder should be empty.
After that you need to insert your api key to 'config.json', which should look like:
### {"api_key" : "your_key_here"}
Then you just need to run "python app.py" in the root directory of the project.

For further help, please refer to the help command in the program.