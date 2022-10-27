from time import sleep  # import sleep to add a pause of displaying tex

# intro function for game introduction
def intro():
    print("\nWelcome to my Quiz Game")
    print("\nThere are 5 questions and you need to answer at least 3 correctly to passed.")
    print("Are you ready?")
    
    # player is asked if he/she wants to play the game
    player = input("\nType y/n: ")
    if player.lower() == "y":   # input is automatically changed to lowercase
        game()                  # player will be directed to the game function
    else:                       # this will end the game instantly
        print("\nMaybe your busy. You can play next time.")

def game():
    score = 0  # variable where total count of correct answer will be stored
    correct_answer = "You are correct!"   # this will displayed if the player guessed correctly
    wrong_answer = "Wrong answer!The correct answer is " #this will be displayed if the player guessed wrong
    name = input("\nInput your name: ") # input player name
    sleep(1)          # 1 sec pause
    print(f"\nWELCOME {name}!!!")
    sleep(1)

    # player starts to answer the questions
    print("\nQuestion # 1: Software is written by software developers using computer-readable code called a(n) _______.")
    question1 = "A. Programming language\nB. Update\nC. Software\nD. Custom"
    print(question1)
    sleep(1)

    guess = input("\nYour answer: ")
    if guess.lower() == "a":
        print(correct_answer)
        sleep(2)
        score += 1   # score was added every correct answer
    else:
        print(f"{wrong_answer}A.")
        sleep(2)

    print("\nQuestion # 2: Which of the following is not one of the principles of good coding?")
    question2 = "A. Create unit tests before you begin coding.\nB. Create unit tests before you begin coding.\nC. Refractor the code after you complete the first coding pass.\nD. Write self-documenting code, not program documentation."
    print(question2)
    sleep(1)

    guess = input("\nYour answer: ")
    if guess.lower() == "c":
        print(correct_answer)
        sleep(2)
        score += 1
    else:
        print(f"{wrong_answer}C.")
        sleep(2)

    print("\nQuestion # 3: The first phase of software development is ______?")
    question3 = "A. Coding\nB. Testing\nC. Design\nD. Requirement analysis"
    print(question3)
    sleep(1)

    guess = input("\nYour answer: ")
    if guess.lower() == "d":
        print(correct_answer)
        sleep(2)
        score += 1
    else:
        print(f"{wrong_answer}D.")
        sleep(2)

    print("\nQuestion # 4: Software engineering primarily aims on ________?")
    question4 = "A. Reliable and cost effective software\nB. Cost effective software\nC. Reliable software\nD. None of these"
    print(question4)
    sleep(1)

    guess = input("\nYour answer: ")
    if guess.lower() == "a":
        print(correct_answer)
        sleep(2)
        score += 1
    else:
        print(f"{wrong_answer}A.")
        sleep(2)

    print("\nQuestion # 5: _____is the illegal copying, distribution, or use of software.")
    question5 = "A. Software Copying\nB. Software Phishing\nC. Digital Piracy\nD. Software piracy"
    print(question5)
    sleep(1)

    guess = input("\nYour answer: ")
    if guess.lower() == "c":
        print(correct_answer)
        sleep(2)
        score += 1
    else:
        print(f"{wrong_answer}C.")
        sleep(2)
    

    print(f"\nYour total score is: {score} out of 5")
   

    if score >= 3:      # if the players total score is 3 and above
        print("\nCongratulations! You passed.")    # displays passed, game ends
    else:
        print("\nSorry, you failed.")    # if the total score is less than 3, displays failed
                                         # GAME ENDS
     
 
# calling the intro function
intro()


