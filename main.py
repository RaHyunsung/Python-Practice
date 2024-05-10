import random

# Ask the user their name and save it
username = input("What's your name? ")
print()
# Greet the user and introduce the quiz
print("Hello! {}. This is a quiz about Python.".format(username))
print()

play = "yes"

while play == "yes":
    score = 0
    # Ask the user a question
    response = input("How to add a comment in Python? ")
    print()
    # Tell them the correct answer
    if response == "#":
        print("The answer was #. You are correct!")
        score += 1
    elif response == "":
        print("The answer was #. You skipped the question!")
    else:
        print("The answer was #. You are incorrect!")

    print(f"How to print 'Hello world!' in Python?\nA. print('Hello world!')\nB. input('Hello world!')\nC. print(Hello world!)")
    response_question2 = input(">  ")
    print()
    # Tell them the correct answer
    if response_question2.lower() == 'a':
        print('The answer was a. You are correct!')
        score += 1
    elif response_question2 == "":
        print('The answer was a. You skipped the question!')
    else:
        print('The answer was a. You are incorrect!')

    response_question3 = input("How to get user input? (Type with brackets) ")
    print()
    # Tell them the correct answer
    if response_question3 == "input()":
        print("The answer was input(). You are correct!")
        score += 1
    elif response_question3 == "":
        print("The answer was input(). You skipped the question!")
    else:
        print("The answer was input(). You are incorrect!")

    response_question4 = input("What symbol suggests string? (Enter only one character) ")
    print()
    # Tell them the correct answer
    if response_question4 == '"':
        print('The answer was ". You are correct!')
        score += 1
    elif response_question4 == "":
        print('The answer was ". You skipped the question!')
    else:
        print('The answer was ". You are incorrect!')

    response_question5 = input("What symbol do I have to use to make a variable? ")
    print()
    # Tell them the correct answer
    if response_question5 == "=":
        print("The answer was =. You are correct!")
        score += 1
    elif response_question5 == "":
        print("The answer was =. You skipped the question!")
    else:
        print("The answer was =. You are incorrect!")

    response_question6 = input("What is the file extension of the Python file? (include dot) ")
    print()
    # Tell them the correct answer
    if response_question6 == ".py":
        print("The answer was .py. You are correct!")
        score += 1
    elif response_question6 == "":
        print("The answer was .py. You skipped the question!")
    else:
        print("The answer was .py. You are incorrect!")

    response_question7 = input("Expert question! How to loop in Python? (only the first three letters) ")
    print()
    # Tell them the correct answer
    if response_question7 == "for":
        print("The answer was for. You are correct!")
        score += 1
    elif response_question7 == "":
        print("The answer was for. You skipped the question!")
    else:
        print("The answer was for. You are incorrect!")

    response_question8 = input("Expert question! How to loop over and over again? (only the five three letters) ")
    print()
    # Tell them the correct answer
    if response_question8 == "while":
        print("The answer was while. You are correct!")
        score += 1
    elif response_question8 == "":
        print("The answer was while. You skipped the question!")
    else:
        print("The answer was while. You are incorrect!")

    response_question9 = input("Expert question! How to make a multiple line string? (only three characters) ")
    print()
    # Tell them the correct answer
    if response_question9 == '"""':
        print('The answer was """. You are correct!')
        score += 1
    elif response_question9 == "":
        print('The answer was """. You skipped the question!')
    else:
        print('The answer was """. You are incorrect!')

    response_question10 = input("Most hardest question! How to use a module in Python? (only six first characters) ")
    print()
    # Tell them the correct answer
    if response_question10 == "import":
        print("The answer was import. You are correct!")
        score += 1
    elif response_question10 == "":
        print("The answer was import. You skipped the question!")
    else:
        print("The answer was import. You are incorrect!")

    number = random.randint(0, 11)
    guess = input("Gamble time! Guess the number (1~10): ")
    if int(guess) == number:
        print("WOW you guessed it! I will double your score for you!")
        score = score * 2
    else:
        print("So close T^T. Try next time. The number was {}".format(number))

    # End the quiz
    print("Great job! Your score is {}!".format(score))
    if score < 9:
        print("New Award! You are a Python expert!")
    play = input("Do you wanna play again? ").lower()