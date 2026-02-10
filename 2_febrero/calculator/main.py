# Version 2.0

def addition (a, b):
	return a + b

def subtract (a, b):
	return a - b

def multiplication (a, b):
	return a * b

def division (a, b):
	if b == 0:
		print("Division by zero!! Try again please")
	return a / b

startCalculator = True
cutPrint = "-" * 20
print("Naka dev calculator! The best calculator around the world!\n" + cutPrint)

while startCalculator:
	try:
		num1 = float(input("Type the first number: "))
		num2 = float(input("Type the second number: "))
		print(cutPrint)
	except(ValueError):
		print(cutPrint + "\nPlease, check the numbers, maybe you are typing non numeric data\n" + cutPrint)

	print("+. Addition")
	print("-. Subtraction")
	print("*. Multiplication")
	print("/. Division")
	print(cutPrint)
	selectOperator = input("Select operation: ")

	if selectOperator != '+' and selectOperator != '-' and selectOperator != '*' and selectOperator != '/':
		print("You must type a valid operator! Please check the options ")
	elif selectOperator == '+':
		addition(num1, num2)
	elif selectOperator == '-':
		subtract(num1, num2)
	elif selectOperator == '*':
		multiplication(num1, num2)
	elif selectOperator == '/':
		division(num1, num2)


