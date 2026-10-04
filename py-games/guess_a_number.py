import random

top_of_range = None

while True:
    top_of_range = input("Type a number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range > 0:
            break
        else:
            print("Please type number above 0")

    else:
        print("Please type a number")

secret_number = random.randint(0, top_of_range)

guessing_number = None
count = 0
while guessing_number != secret_number:
    guessing_number = input("Guess a number: ")

    if not guessing_number.isdigit():
        print("Please type a number")
        continue

    guessing_number = int(guessing_number)

    if guessing_number > secret_number:
        print("Number is too high")

    elif guessing_number < secret_number:
        print("Number is too low")

    else:
        print("You guessed the number!")
    count +=1
print(f"It took you {count} tries to get the number.")


