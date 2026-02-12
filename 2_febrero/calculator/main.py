# Version 2.0

def addition (a, b):
	return a + b

def subtract (a, b):
	return a - b

def multiplication (a, b):
	return a * b

def division (a, b):
	return a / b

startCalculator = True
areNumbers = True
cutPrint = "-" * 20
print("Naka dev calculator! The best calculator around the world!\n" + cutPrint)

while startCalculator:
	while areNumbers:
		try:
			num1 = float(input("Type the first number: "))
			num2 = float(input("Type the second number: "))
			areNumbers = False
			print(cutPrint)
		except (ValueError):
			print(cutPrint)
			print("Please, type only digits")
			print(cutPrint)

	print("+. Addition")
	print("-. Subtraction")
	print("*. Multiplication")
	print("/. Division")
	print(cutPrint)
	selectOperator = input("Select operation: ")

	if selectOperator != '+' and selectOperator != '-' and selectOperator != '*' and selectOperator != '/':
		# if selectOperator not in ['+', '-', '*', '/']: I can use this structure
		print("You must type a valid operator! Please check the options ")
	elif selectOperator == '+':
		print(addition(num1, num2))
	elif selectOperator == '-':
		print(subtract(num1, num2))
	elif selectOperator == '*':
		print(multiplication(num1, num2))
	elif selectOperator == '/':
		if num2 == 0:
			print("Cannot divide by zero!")
		else:
			print(division(num1, num2))

	finishCalculator = input("Press 'Enter' to continue or 'q' to exit: ")
	print(cutPrint)

	if finishCalculator.lower() == 'q':
		startCalculator = False
	else:
		areNumbers = True
		continue