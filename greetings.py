# Define the Greeting Function ==========================
def greet(sentence):
  import random
  Greet_Inputs = ("hello","hi","hey","greetings","hello there","whats up")
  Greet_Responses = ("Hi","Hi there","Hey","Hello","Hello there","I'm glad! You are talking to me.", "Hello! How can I help you?")
  for word in sentence.split():
    if word.lower() in Greet_Inputs:
      return random.choice(Greet_Responses)