import random


print("Welcome to Guess the Number! 🎯")
print("Can you beat the computer's secret number? 🤔")

print("Choose a difficulty level:")
print("1. Easy 🌱: 1-20")
print("2. Medium ⚡: 1-50")
print("3. Hard 🔥: 1-100")

difficulty = input("Enter 1, 2, or 3: ")

# Choose the largest possible number based on the difficulty.
if difficulty == "1":
    max_number = 20
elif difficulty == "2":
    max_number = 50
else:
    max_number = 100

# The computer chooses a random number in the selected range.
secret_number = random.randint(1, max_number)

# This variable counts how many guesses the player makes.
attempts = 0

print("I am thinking of a number between 1 and", max_number, "🧠")
print("Good luck! 🍀")

# Keep asking the player to guess until they find the correct number.
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Aim higher. ⬆️")
    elif guess > secret_number:
        print("Too high! Come down a bit. ⬇️")
    else:
        print("Correct! You guessed the number! 🎉")
        print("It took you", attempts, "attempts. ⭐")
        break
