guesses = []
FAMOUS_LANGUAGES = [
    "Python",
    "C",
    "C++",
    "C#",
    "Lua",
    "PHP",
    "JavaScript",
    "Java",
    "Go",
    "Ruby",
    "SQL",
    "R",
    "Rust",
    "TypeScript",
    "VBA",
    "Assembly"
]

# ----- FUNCTIONS -----

# Welcome user and introduce the quize
def intro():
    # Ask the user their name
    name = input("What's your name? ")

    # Greet the uer and introduce the quiz
    print("Welcome to this quiz, ", name)
    print("This quiz is about the top 10 popular programming lanugages.")

# Ask user for lives and confirms is valid
def getLives():
    while True:
        lives = input("How many chances do you want? ")
        try:
            # Checking if valid number
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number.")
        except:
            print("That wasn't a number.")

def inList(answer, list):
    list = [str(element).lower() for element in list]
    answer = answer.lower()
    if answer in list:
        return True
    else:
        return False

# ----- MAIN CODE -----

intro()

lives = getLives()
score = 0

# Begin quiz 
while True:
    if lives <= 0:
        break
    answer = input("Name one of the top 10 most famous programming langueages in the world:\n").lower()
    if inList(answer, FAMOUS_LANGUAGES) == True:
        # Checks if already guessed or not
        if inList(answer, guesses):
            print("You've guessed that already.")
        else:
            print("Correct")
            score += 5
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} chances remaining.".format(len(guesses), score, lives))
    else:
        print("Wrong")
        lives -= 1
        print("You have guessed {}. Your score is {}. You have {} chances remaining.".format(len(guesses), score, lives))

print("Game Over. Your fnal score was {}.".format(score))