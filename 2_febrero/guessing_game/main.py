import random

# Define a random number between 0 and 10 
randomNum = random.randrange(0,10,1)
print(randomNum)

# Variables
startGame = True
cutPrint = "-" * 30

print("Hi! I'd generated 3 random numbers! 😈")
print("If you guess 2 times you'll winner!!!")
print(cutPrint)

userOption = input("Do you want to try? 😈\nPress 'Enter' to start or Type 'q' to exit: ")

if userOption.lower() == 'q':
  startGame = False
else:
  while startGame:
    print("Empezó el game")