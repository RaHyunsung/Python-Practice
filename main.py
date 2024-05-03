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
elif response == "":
    print("The answer was #. You skipped the question!")
else:
    print("The answer was #. You are incorrect!")

response_question2 = input("How to print 'Hello world!' in Python? ")
print()
# Tell them the correct answer
if response_question2 == 'print("Hello world!")':
    print('The answer was print("Hello world!"). You are correct!')
elif response_question2 == "":
    print('The answer was print("Hello world!"). You skipped the question!')
else:
    print('The answer was print("Hello world!"). You are incorrect!')

response_question3 = input("How to get user input? (Type with brackets) ")
print()
# Tell them the correct answer
if response_question3 == "input()":
    print("The answer was input(). You are correct!")
elif response_question3 == "":
    print("The answer was input(). You skipped the question!")
else:
    print("The answer was input(). You are incorrect!")

response_question4 = input("What symbol suggests string? (Enter only one character) ")
print()
# Tell them the correct answer
if response_question4 == '"':
    print('The answer was ". You are correct!')
elif response_question4 == "":
    print('The answer was ". You skipped the question!')
else:
    print('The answer was ". You are incorrect!')

response_question5 = input("What symbol do I have to use to make a variable? ")
print()
# Tell them the correct answer
if response_question5 == "=":
    print("The answer was =. You are correct!")
elif response_question5 == "":
    print("The answer was =. You skipped the question!")
else:
    print("The answer was =. You are incorrect!")

response_question6 = input("What is the file extension of the Python file? (include dot) ")
print()
# Tell them the correct answer
if response_question6 == ".py":
    print("The answer was .py. You are correct!")
elif response_question6 == "":
    print("The answer was .py. You skipped the question!")
else:
    print("The answer was .py. You are incorrect!")

response_question7 = input("Expert question! How to loop in Python? (only the first three letters) ")
print()
# Tell them the correct answer
if response_question7 == "for":
    print("The answer was for. You are correct!")
elif response_question7 == "":
    print("The answer was for. You skipped the question!")
else:
    print("The answer was for. You are incorrect!")
# End the quiz