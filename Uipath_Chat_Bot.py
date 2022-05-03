import requests
from nltk.chat.util import Chat, reflections
import Uipath_functions

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Makelly and I'm a chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
     [
        r"(.*)good|(.*)fine",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hi",]
    ],  
   [
        r"quit",
        ["Thanks for interacting with me! Have a Nice Day"]
    ],
    [
        #to get list of all queue names from orchestrator
        r"(.*)queue names",
        [Uipath_functions.QueueNames()]
    ],
       
    [
        # to get list of all process and their versions
        r"(.*)list(.*)process",
        [Uipath_functions.ProcessList()]
    ],

    [
        # to get bot error logs
        r"(.*)bot logs",
        [Uipath_functions.ErrorLogs()]
    ],
    [
        r"(.*)process version",
        [Uipath_functions.ProcessVersion()]
    ],
]

def main():
    print("Hi, I'm ChatBot\n I can help you with Uipath Robot and process detais ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

    
if __name__ == "__main__":
    main()

    
    
