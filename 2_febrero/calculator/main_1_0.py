# Version 1.0

def addition (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiplication (a, b):
    return a * b

def division (a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

startCalculator = True
while startCalculator:
    startCalculator = input("Welcome to the calculator program!\nPress q to exit.\nPress Enter to continue\n" + "-" * 20 + "\n")

    if startCalculator.lower() == 'q':
        startCalculator = False
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        continue

    if num2 == 0:
        print("Invalid input! Please enter numeric values.")
    else: 
        print("Select operation")
        print("+. Addition")
        print("-. Subtraction")
        print("*. Multiplication")
        print("/. Division")
        print("-" * 20)
        operation = input ("Enter operator ")

        if operation == "+":
            result = addition(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiplication(num1, num2)
        elif operation == "/":
            result = division(num1, num2)
        else:
            print("Invalid operation")
        print("-" * 20)
        
        try:    
            print(f"Result: {result}\n" + "-" * 20)
        except NameError:
            print("Error: No result to display.")