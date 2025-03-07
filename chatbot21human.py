import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"Hi|Hello|Hey", ["Hello! How can I assist you today?", "Hi there! How can I help you?"]),
    (r"Good morning", ["Good morning! How can I make your day better?"]),
    (r"How are you?", ["I'm doing great, thank you for asking!", "I'm doing well, how about you?"]),
    (r"What's your name?", ["I'm a chatbot, I don't have a name, but you can call me ChatBot."]),
    (r"(.*) your name?", ["I am a chatbot, and I don't have a name."]),
    (r"(.*) help (.*)", ["Sure, I am here to help! What do you need help with?"]),
    (r"Tell me a joke", ["Why don’t skeletons fight each other? They don’t have the guts!", "Why did the math book look sad? Because it had too many problems!"]),
    (r"Give me some advice", ["Stay positive and keep learning!", "The only way to do great work is to love what you do."]),
    (r"What's the weather like?", ["I don't have access to live weather data, but you can check a weather app or website!"]),
    (r"Tell me something interesting", ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!"]),
    (r"Bye|Quit", ["Goodbye! Have a great day!", "Bye! Take care!"]),
    (r"(.*)", ["Sorry, I didn't quite understand that. Can you rephrase it?"]),
]
def chatbot():
    print("ChatBot: Hi! Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()