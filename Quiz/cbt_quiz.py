import random
import time

score = 0

print("============================================")
print("     WELCOME TO THE CBT APPLICATION")
print("============================================")
print("\nSubject: General Knowledge")
print("Number of Questions: 5")
print("Each question carries 10 marks")

name = input("\nEnter your name: ")
print("Student:", name)

input("\nPress Enter to CONTINUE...")

questions = [
    "Which planet in our solar system is known as the Red Planet?",
    "Who painted the famous artwork known as the Mona Lisa?",
    "What is the tallest mountain in the world by height above sea level?",
    "What is the chemical symbol for gold on the periodic table?",
    "Which is the longest river in the world?"
]

options = [
    "A) Venus\nB) Mars\nC) Jupiter\nD) Saturn",
    "A) Vincent van Gogh\nB) Pablo Picasso\nC) Leonardo da Vinci\nD) Claude Monet",
    "A) K2\nB) Mount Kilimanjaro\nC) Mount Everest\nD) Denali",
    "A) Go\nB) Gd\nC) Au\nD) Ag",
    "A) Amazon River\nB) Nile River\nC) Yangtze River\nD) Mississippi River"
]

answers = [
    "B",
    "C",
    "C",
    "C",
    "B"
]

# Combine everything together
quiz = list(zip(questions, options, answers))

# Shuffle the questions
random.shuffle(quiz)

# Separate them again
questions, options, answers = zip(*quiz)

questions = list(questions)
options = list(options)
answers = list(answers)

# Store student answers
student_answers = []

# 6-minute timer
exam_time = 360
start_time = time.time()

# Quiz starts here
for i in range(len(questions)):

    elapsed_time = time.time() - start_time
    remaining_time = exam_time - elapsed_time

    if remaining_time <= 0:
        print("\nTIME IS UP!")
        break

    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)

    print(f"\nTime Remaining: {minutes:02}:{seconds:02}")

    print("\n--------------------------------------------")
    print("Question", i + 1)
    print("--------------------------------------------")
    print(questions[i])
    print(options[i])

    answer = input("\nAnswer: ").upper()

    student_answers.append(answer)

    if answer == answers[i]:
        score += 10

print("\n============================================")
print("             EXAM COMPLETED")
print("============================================")

print("\n============================================")
print("                RESULTS")
print("============================================")

print("Student:", name)
print("Score:", score, "/50")

percentage = (score / 50) * 100
print("Percentage:", percentage, "%")

print("\n============================================")
print("             RESULT REVIEW")
print("============================================")

for i in range(len(student_answers)):
    print("\nQuestion", i + 1)
    print(questions[i])
    print("Your Answer:", student_answers[i])
    print("Correct Answer:", answers[i])

    if student_answers[i] == answers[i]:
        print("Result: Correct")
    else:
        print("Result: Wrong")

# Save result
with open("results.txt", "a") as file:
    file.write(f"{name} - {score}/50 - {percentage:.1f}%\n")

input("\nPress Enter to exit...")