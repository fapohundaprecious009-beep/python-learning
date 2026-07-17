score = 0
print("============================================")
print("     WELCOME TO THE CBT APPLICATION")
print("============================================")
print("\nSubject: General Knowledge")
print("Number of Questons: 5")
print("Exach question carries 10 marks")

name=input("\nEnter your name: ")
print("Student: \n", name)

print("\nQuestion 1: ")
print("\nWhat is the capital of Nigeria?")
print("A. Lagos \nB. Abuja \nC. Kano \nD. Ibadan")
answer = input("\nAnswer: ").upper()
if answer == "B":
    print("correct")
    score += 10
else:
    print("wrong \nCorrect Answer: B. Abuja")

print("\nQuestion 2: ")
print("\nWhich is a not a protein?")
print("A. Rice \nB. Beans \nC. Egg \nD. Milk")
answer = input("\nAnswer: ").upper()
if answer == "A":
    print("correct")
    score += 10
else:
    print("wrong \nCorrect Answer: A. Rice")

print("\nQuestion 3: ")
print("\nWhich is the smallest planet?")
print("A. Venus \nB. Jupiter \nC. Mars \nD. Pluto")
answer = input("\nAnswer: ").upper()
if answer == "D":
    print("correct")
    score += 10
else:
    print("wrong \nCorrect Answer: D. Pluto")

print("\nQuestion 4: ")
print("\nWhat programming language do they use 'printf'?")
print("A. C++ \nB. Java \nC. C \nD. Python")
answer = input("\nAnswer: ").upper()
if answer == "C":
    print("correct")
    score += 10
else:
    print("wrong \nCorrect Answer: C. C")

print("\nQuestion 5: ")
print("\nA______is a program in execution")
print("A. passive program \nB. process \nC. processor \nD. Python")
answer = input("\nAnswer: ").upper()
if answer == "B":
    print("correct")
    score += 10
else:
    print("wrong \nCorrect Answer: B. process")

print("\nEXAM COMPLETED\n")

print("============================================")
print("                  RESULTS")
print("============================================")
print("Student: ", name)
print("Score: ", score, "/50")
percentage = (score/50) * 100
print("Percentage: ", percentage, "%")


