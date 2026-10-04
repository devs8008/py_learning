import random
# This will be a python game using conditional statements and Loops.

start = input("Do you wanna play a game? (yes/no): ").lower()

if start != "yes":
    print("Maybe next time!")
    quit() # Terminates the whole program nothing else will be executed after this point. It is not recomended to use quit() in production code, but it is fine for small scripts and games.
else:
    print("Great! Let's start the game.")
    print("You have to guess a number between 1 and 10.")
    secret_number = random.randint(1, 10) # To get a random whole number from 1 to 10
    attempts = 3

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Congratulations! You've guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print("Sorry, you've run out of attempts. The correct number was:", secret_number)