score = 0      # global variable used to store the total accummulated points

# intro function for game introduction
def intro():
    print("""
    WELCOME TO MY SURVEY TRIVIA GAME!!!\n
    ===> In this game, you will try to guess the most popular answer based on the survey we conducted to 100 people.
    ===> Each correct answer has an equivalent points.
    ===> You will win the game if you collect at least 500 points.
    ===> There are 3 rounds. If you answered wrong 3 times, round ends and will proceed to the next round.
    Are you ready for the challenge?""")

    start = input("\nType y: ").lower()
    if start == "y":      # if answer "y", game will proceed to round 1
        round1()
    else:
        print("You're so boring! Hope you have a good day!")    # this will instantly end the game

# this is the first round
def round1():
    global score   
    strikes = 3       # number of times the player is allowed to answer incorrectly
    languages = ["python", "javascript", "ruby", "java", "c++"]  # lists of words that needs to guess
    points = [60, 20, 10, 5, 4]                                     # corresponding points
    
    print("\nQUESTION # 1: We surveyed 100 software engineers, what is their top 5 favorite programming languages?")
    correct_answer = True
    
    # loop until the player guessed all the correct answer
    while correct_answer:
   
        answer = input("\nYour answer: ").lower()  # answer is automatically changed to lowercase
        if answer in languages:                    # if the answer is in the list
                    index = languages.index(answer)   # to check in what position the answer is in the list
                    points_earned = int(points[index])    # convert the corresponding points to integer
                    score += points_earned                # points earned are added to the score
                    languages.remove(answer)              # every correct answer is remove from the list
                    points.remove(points[index])          # also the corresponding points is removed
                    
                    # if condition to check if the list is already empty
                    if languages != []:      
                        print(f"Correct! You got the answer. It is worth {points_earned} points.")  # is not yet empty, display this
                    else:
                        print("You got all the answer.")  # if the list is already empty
                        print(f"Current score: {score}")  # display this
                        print("Time for the next round")
                        round2()                          # calling round2() function, game will proceed to round 2
                        break                             # while loop will break here
        
        else:     # if the player guessed wrong
                print(f"You answered wrong!") 
                strikes -= 1      # number of strikes is decreased by 1
                if strikes == 0:  # if all the strikes are used(answered wrong 3 times)
                    print("\nThree strikes")
                    print(f"Time for the next round.")
                    print(f"Current score: {score}")
                    round2()       # game will proceed to round 2
                    break
def round2():
    global score 
    strikes = 3
    tools = ["git", "github", "visual studio", "stack overflow", "jira"]
    points = [50, 25, 15, 5, 4]# can make dictionary
    
    print("\nWE ARE NOW IN ROUND 2")
    print("In this round, points are doubled so you have more chances to win.")
    print("QUESTION # 2: We surveyed 100 software engineers, what are the most popular productivity tools that they use?")
    correct_answer = True

    while correct_answer:
   
        answer = input("\nYour answer: ").lower()  
        if answer in tools:             
                    index = tools.index(answer)   
                    points_earned = int(points[index])   
                    score += points_earned  * 2             
                    tools.remove(answer) 
                    points.remove(points[index])           
                    
                    if tools != []:
                        print(f"That's correct. It is worth {points_earned} points.")
                    else:
                            print("You got all the answer.")
                            print(f"Current score: {score}")
                            print("Time for the next round")
                            round3()
                            break
        else:
                print(f"Sorry, it's not in the list!") 
                strikes = strikes - 1  
                if strikes == 0:
                    print("\nThree strikes")
                    print(f"Time for the next round.")
                    print(f"Current score: {score}")
                    round3()
                    break

def round3():
    global score
    strikes = 3
    salary = ["40000", "50000", "60000", "70000"]
    points = [60, 20, 5, 3]
    
    print("\nWE ARE NOW IN ROUND 3, THE FINAL ROUND")
    print("\nIn this round, points are tripled so you have higher chances of winning.")
    print("QUESTION # 3: We surveyed 100 software engineers, what is their average salary per month?")
    correct_answer = True

    while correct_answer:
   
        answer = input("\nYour answer: ").lower() 
        if answer in salary:             
                    index = salary.index(answer)   
                    points_earned = int(points[index])   
                    score += points_earned * 3          
                    salary.remove(answer) 
                    points.remove(points[index])            
                    
                    if salary != []:
                        print(f"Correct! It is worth {points_earned} points.")
                    else:
                            print("You got all the answer.")
                            print(f"Current score: {score}")
                            total_score()
                            break
        else:
                print(f"Tooot, wrong answer!") 
                strikes = strikes - 1   
                if strikes == 0:
                    print("\nThree strikes")
                    print(f"Current score: {score}")
                    total_score()
                    break

def total_score():
    global score
    final_score = score    # this is the total accummulated points
    print(f"\nYour total points is: {final_score}")
    finish = True

    while finish:
        if final_score >= 500:        # if the total points earned is greater than or equal to 500
            print("\nCongratulations! You win.")   
            break                     # end of the game
        else:
            print("\nOh! I'm sorry, you didn't win.")    # if the total points is less than 500
            break                     # end of the game


intro()