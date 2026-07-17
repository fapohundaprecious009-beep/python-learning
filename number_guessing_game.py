
import random

secret_number = random.randint(1, 100)

print("===================================================")
print("       WELCOME TO THE NUMBER GUESSING GAME")
print("===================================================")
print("RULES OF THE GAME:")
print("1. You are to guess a number between 1 to 100")
print("2. You have just 10 attempts to guess the number")

for i in range(10):

    guess= int(input("Guess a number: "))

    if guess==secret_number:
        print("You won the game")
        break
    elif guess<secret_number:
        print("It is too low")
    else:
        print("It is too high")

else:
    print("GAME OVER")
