import random

questions = [
    ["How to add a comment in Python? ", "#"],
    ["How to print 'Hello world!' in Python?\nA. print('Hello world!')\nB. input('Hello world!')\nC. print(Hello world!)\n> ", "a"],
    ["How to get user input? (Type with brackets) ", "input()"],
    ["What symbol suggests string? (Enter only one character) ", '"'],
    ["What symbol do I have to use to make a variable? ", "="],
    ["What is the file extension of the Python file? (include dot) ", ".py"],
    ["Expert question! How to loop in Python? (only the first five letters starts with letter w) ", "while"],
    ["Expert question! How to make a multiple line string? (only three characters) ", '"""'],
    ["Most hardest question! How to use a module in Python? (only six first characters) ", "import"]
]

# Ask the user their name and save it
username = input("What's your name? ")
print()
# Greet the user and introduce the quiz
print("Hello! {}. This is a quiz about Python.".format(username))
print()

while True:
    try:
        tries = input("How many attempts do you want at each questions? 1~4 ")
        tries = int(tries)
        if tries < 5:
            break
        else:
            print("That's to much.")
    except:
        print("That's not a number.")

play = "yes"

while play == "yes":
    score = 0
    for question in questions:
        ask = question[0]
        answer = question[1]
        for i in range(tries): # Repeat attempts
            response = input(ask)
            # Ask the user a question
            if response.lower() == answer:
                print("You are correct!")
                score += 1
                break
            elif response == "":
                print("You skipped the question.")
                break
            else:
                print("Incorrect. Please try again. Attmept remaining: {}/{}".format(4-i-1, tries))
                continue
        # Tell them the correct answer
        print("The correct answer was {}! Your current score is {} out of {}!".format(answer, score, len(questions)))
        print()

    number = random.randint(0, 11)
    guess = input("Gamble time! Guess the number (1~10): ")
    try:
        if int(guess) == number:
            print("WOW you guessed it! I will double your score for you!")
            score = score * 2
        else:
            print("So close T^T. Try next time. The number was {}".format(number))
    except:
        print("So close T^T. Try next time. The number was {}".format(number))

    # End the quiz
    print("Great job! Your score is {} out of {}!".format(score, len(questions)))
    if score < 9:
        print("New Award! You are a Python expert!")
    play = input("Do you wanna play again? ").lower()

print("Thank you for playing this quiz!")