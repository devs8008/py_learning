# Lets say this is the starting point of our game. We will have a main function that will be called when the game starts.
# NOTE And we dont want any file that imports this file to start our game automatically. So we will use the if __name__ == "__main__": statement to check if this file is being run directly or imported.

def main():
    print("Welcome to the game!")
    # This message will mean that this is being run directly and we can start the game.
    print("Game is starting...")

if __name__ == "__main__":
    main()
# NOTE When this file is run directly, python interprater will assign the string "__main__" to the built-in variable __name__. So the if statement will evaluate to True and the main function will be called. If this file is imported into another file, the __name__ variable will be assigned the name of this file (game) and the if statement will evaluate to False and the main function will not be called.