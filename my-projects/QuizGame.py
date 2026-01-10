print("------------------------------ ")
k = "Welcome to the Quiz Game!"
print(k.upper())
print("------------------------------ ")
play = input("\n\n Do you want to play the game (yes/no)? ")
if play.lower() == "yes":
    print("\nOkay! Let's play the game!")
    score = 0

    answer = input("\n1. What is the name of the final messenger of Allah? ")
    if answer.upper() == "MUHAMMAD":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is MUHAMMAD.")

    answer = input("\n2. How many times do we pray our obligatory prayers in a day? ")
    if answer == "5" or answer == "five":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is 5.")

    answer = input("\n3. What is the name of the holy book of Islam? ")
    if answer.upper() == "QURAN" or answer.upper() == "AL QURAN":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is QURAN.")

    print(f"\nYou got {score} questions correct out of 3.")
    percentage = (score / 3) * 100
    print(f"Your score percentage is: {percentage}%")