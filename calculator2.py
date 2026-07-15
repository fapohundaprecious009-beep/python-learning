response = "yes"

while response == "yes":

#Ask the user for two numbers
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second nnumber: "))

#Ask the user to choose an operator
    operator=input("Choose an operator (+, -, *, /): ")

#The if-else statement when an operator is chosen
    if(operator == "+"):
        print("The answer is: ", num1+num2)
    elif(operator=="-"):
        print("The answer is: ", num1-num2)
    elif(operator=="*"):
        print("The answer is: ", num1*num2)
    elif(operator=="/"):
        if num2 == 0:
            print("Division by 0 is not allowed.")
        else:
            print("The answer is: ", num1/num2)
    else:
        print("Invalid operator")


    response = input("Do you want to perform another calculaton? (yes/no): ").lower()

print("Thank you for using the calculator!")


   
