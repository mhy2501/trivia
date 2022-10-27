# import module time
import time

#  Introduction to the game and instructions
print("\n\n\n=================================== WELCOME TO MY HANGMAN GAME! ===========================================================")
time.sleep(5)
print("\nIn this game, you need to guess the correct word to win and take home the pot money of 1 MILLION pesos!")
time.sleep(4)
print("\n==== Can you guess the mystery word??? =====")
time.sleep(4)
print("\nThese are the rules of the game.")
time.sleep(4)
print("====> You are given 30 seconds to guess the word.")
time.sleep(3)
print("====> Words are case-sensitive so please answer only in lower-case letters.")
time.sleep(3)
print("====> You only have 5 attempts, so think carefully before you answer.")
time.sleep(2)
print("\n***** BUT REMEMBER: You only have 30 seconds so keep your brain running.*****")
time.sleep(3)
print(f"\nAre you ready to take the challenge? Type [y] or [n]")
time.sleep(2)


# mystery words that the player will guess randomly
word1 = "python"
word2 = "javascript"
word3 = "java"


# user needs to input y or n to start the game
# this will continue to loop until the user enters n or no
while True:
    user = input()
    if user == "y" or user == "Y" or user == "yes" or user == "YES":
        print("\nLet the game begins!")
        time.sleep(2)
        print("\n**** HINT: This is one of the most popular programming languages today.****")

        #this are the number of chances that will give to the player
        chances = 5
        
        # player will start to guess the mystery word until he/she gets it right or use all of the chances given
        for num in range(1,chances + 1):
            guess = input("\nYour guess: ")
            time.sleep(2)

            if num != chances:
   
                # if the player guesses the correct word before using up all of the chances, for loop will break and the player can start again the game if he/she wants
                if guess == word1 or guess == word2 or guess == word3:
                    print("Congratulations!!! You did it. Your such a genius.\n\nDo you want to play again?\n")
                    break
            
                # if the player guesses wrong, he/she will be given another chance until all the chances are used up
                elif guess != word1 or guess != word2 or guess != word3:
                    print("Oh! oh! That is wrong. Try again.")

            # if the player guessed one of the correct word in her/his last attempt
            elif num == chances:
                if guess == word1 or guess == word2 or guess == word3:
                    print("That was nerve-racking! You almost lost your chance, but you made it. Congratulations!!!\n\nDo you want to play again?\n")
                
            # if the player guesses wrong 5 times, for loop will break and ask the player if he/she want to try again
                elif guess != word1 or guess != word2 or guess != word3:
                    print("Sorry!!! You used up all of your chances...\n\nDo you want to play again?\n")
                    break

    # this will break the entire loop and end the game
    elif user == "n" or user == "N" or user == "no" or user == "NO":
        print("\n\n======================================= THIS ENDS HERE! ==========================================================\n\n")
        break

    # if the player entered other characters aside from y or n
    else:
        print("\nEnter only [y] or [n]...")
