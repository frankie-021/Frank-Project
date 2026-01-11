import random
import time
print(" ---- HELLO! WELCOME TO THE NUMBER GUESSING GAME ---- \n")

play = input("Do you want to play the game(yes/no)? ")
if play.lower() == "yes":
    print("Ok! Let the game begin\n")
    
    range = input("Type the range of the guessing numbers you prefer. ")
    if range.isdigit:
        range = int(range)
        if range <= 0:
            print("Sorry! Number should be greater than 0. Try again.")
            quit()
    else:
        print("Please the value should be a number.")
        quit()
    random_number = random.randint(0, range)
    guess_scored = 0        
        
    while 1:
        guess_scored += 1
        guess = input("Guess the number. ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Value shoud be a number.")
            continue
        if guess == random_number:
            print(f"Random number is {random_number}")

            for i in range (3,0,-1):
                print(i)
                time.sleep(1)
            print(f"Congrats! You got it correct.")
            break
        else:
            print("Oops! wrong guessing.")
    print(f"total guess is {guess_scored}")
print("Exit.")
    

