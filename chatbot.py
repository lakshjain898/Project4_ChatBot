import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"how are you ?",
        ["I'm just a program, but I'm doing fine. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries.", "No problem at all!"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that! How can I assist you today?",]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot. You can call me HelperBot!",]
    ],
    [
        r"how can I (.*)",
        ["You can try searching for resources online or let me know your specific query.",]
    ],
    [
        r"(.*) created you ?",
        ["I was created by a developer using Python and NLTK.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm in the virtual world, helping users like you.",]
    ],
    [
        r"quit",
        ["Bye! Have a great day.", "Goodbye! Take care."]
    ],
]

# Default responses for unknown queries
default_response = "I'm sorry, I don't understand that. Can you please rephrase?"

# Creating the chatbot
def chatbot():
    print("Hi! I am your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
