
# Create a game where the computer selects a number and the user tries to guess it.

secret_number = 7

while True:
    guess = int(input("Enter the Guess Number :: "))

    if guess > secret_number:
        print("Too High")

    elif guess < secret_number:
        print("Too Low")

    else:
        print("You Win")
        break

