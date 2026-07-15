
import random

secret_number = random.randint(1, 100)

print("===================================================")
print("       WELCOME TO THE NUMBER GUESSING GAME")
print("===================================================")
print("RULES OF THE GAME:")
print("1. You are to guess a number between 1 to 100")
print("2. You have just 5 attempts to guess the number")

guess= int(input("Guess a number: "))

if guess==secret_number:
    print