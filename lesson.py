#range(start,stop,step)
for i in range(5):
    print("Hello")


for  i in range(1,11):
    print(i)

for i in range(2,22,2):
    print(i)

for i in range(20,0,-2):
    print(i)

number = int(input("Enter a number: "))
print("Multiplication Table for ", number)
for i in range(1,12):
    answer = number * i
    print(answer)