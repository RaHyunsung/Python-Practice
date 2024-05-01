# Ask the user their name and save it
username = input("What's your name? ")
print()
# Greet the user and introduce the quiz
print("Hello! {}. This is a quiz about Python.".format(username))
print()
# Ask the user a question
response = input("How to add a comment in Python? ")
print()
# Tell them the correct answer
if response == "#":
    print("The answer was #. You are correct!")
else:
    print("The answer was #. You are incorrect!")
# End the quiz

