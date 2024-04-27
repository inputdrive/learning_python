import random

user_name = input("What is your name? ")
print("Hello, " + user_name + "!")
print("Welcome to the Magic 8 Ball!")
print("Ask me a question and I will tell you the answer.")
question = input(user_name + "What is your question? ")
# List of possible responses
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Generate a random response
response = random.choice(responses)

# Print the response
print("The Magic 8 Ball says:", response)
