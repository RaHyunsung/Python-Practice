import random

QUESTION_FORMAT = "A. {}\nB. {}\nC. {}\n"

QUESTIONS = [
    ["How to add a comment in Python?", "C"],
    ["How to print 'Hello world!' in Python? ", "B"],
    ["How to get user input? (Type with brackets) ", "A"],
    ["What symbol suggests string?", "A"],
    ["What symbol do I have to use to make a variable? ", "C"],
    ["What is the file extension of the Python file?", "B"],
    ["Expert question! How to loop in Python?", "B"],
    ["Expert question! How to make a multiple line string?", "A"],
    ["Most hardest question! How to use a module in Python?", "B"]
]

OPTIONS = [
    ["<!--", "//", "#", "--"],
    ['Helloworld!("print")', 'print("Hello world!")', 'print(Hello world!)'],
    ["input()", "Console.Read()", "getpass.getpass()"],
    ['"', "`", "-"],
    ["->", ">>", "="],
    [".python", ".py", ".exe"],
    ["for", "while", "try"],
    ['"""', "```", "---"],
    ["export", "import", "include"]
]

# ----- FUNCTIONS -----

def intro():
    # Ask the user their name and save it
    username = input("What's your name? ")
    print()

    # Greet the user and introduce the quiz
    print("Hello! {}. This is a quiz about Python.".format(username))
    print()

def getPassword():
    while True:
        password = input("What's the password? ")
        if password == "pwd":
            return
        else:
            print("Nope. Try again.")

def getLives():
    while True:
        lives = input("How many chances do you want? ")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number.")
        except:
            print("That wasn't a number")

intro()
getPassword()
tries = getLives()
tries = tries + 1

play = "yes"

while play == "yes":
    score = 0
    for question in range(len(QUESTIONS)):
        answer = QUESTIONS[question][1]
        for i in range(tries): # Repeat attempts
            print(QUESTIONS[question][0])
            print(QUESTION_FORMAT.format(*OPTIONS[question]))
            response = input("> ")
            # Ask the user a question
            if response.lower() == answer.lower():
                print("You are correct!")
                score += 1
                break
            elif response == "":
                print("You skipped the question.")
                break
            else:
                print("Incorrect. Please try again. Attmept remaining: {}/{}".format(tries-i-1, tries-1))
                continue
        # Tell them the correct answer
        print("The correct answer was {}! Your current score is {} out of {}!".format(answer, score, len(QUESTIONS)))
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
    print("Great job! Your score is {} out of {}!".format(score, len(QUESTIONS)))
    if score < 9:
        print("New Award! You are a Python expert!")
    play = input("Do you wanna play again? ").lower()

print("Thank you for playing this quiz!")