import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

responses = {
    
    "hello": "Hi there!",
    "what is your name?": "My name is Chatbot.",
    "how are you?": "I'm doing well, thanks for asking.",
    "bye": "Goodbye!",
}

user_input = input("What would you like to say?  : ")

tokens = nltk.word_tokenize(user_input)
tagged_tokens = nltk.pos_tag(tokens)

if any(tag.startswith('NN') for word, tag in tagged_tokens):
    response = "I'm sorry, I don't understand."
else:
    response = responses.get(user_input.lower(), "I'm sorry, I don't understand.")

print(response)
