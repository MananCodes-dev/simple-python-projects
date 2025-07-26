#This is my first mini project which is making calcuator
#First let's ask user to enter two numbers
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the Second number"))

# Now let's ask user to enter the operation they want to perform
function = input("Enter the operation you want to perform (+,-,*,/) choose between 1 to 4 ")

#Let's convert the operation to a number
if function == "1":
    print(num1 + num2)
elif function == "2":
    print(num1-num2)
elif function == "3":
    print(num1*num2)
elif function == "4":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose between 1 to 4.")

# This is the code for my first mini projet 