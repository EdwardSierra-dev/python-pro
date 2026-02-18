import random

# Define a random number between 0 and 10
def generateRandomNum():
  return random.randrange(0,10,1)

# Variables
startGame = True
randomNumbers = []
countCorrect = 0
cutPrint = "-" * 30


print(cutPrint)
print("Hi! I'd generated 3 random numbers! 😈")
print("If you guess 2 times you'll winner!!!")
print(cutPrint)

userOption = input("Do you want to try? 😈\nPress 'Enter' to start or Type 'q' to exit: ")

if userOption.lower() == 'q':
  startGame = False
else:
  while startGame:
    countCorrect = 0
    randomNumbers.clear()
    for i in range(3):
      randomNumbers.append(generateRandomNum())
    print(randomNumbers)
    print("Game stared! 😎")
    for i in range(3):
      userNum = int(input(f"Guess the number {i + 1}: "))
      print(cutPrint)
      if userNum == randomNumbers[i]:
        # Claro aquí solo compara en el input con la posición pero necesito buscarlo en todos los indices jeje cagada
        print(cutPrint)
        countCorrect += 1
      else:
          print("Wrong! Try again! 😈")
          print(cutPrint)

    if countCorrect >= 2:
      print("Congratulations! You win! 🥳")
      print(cutPrint)
      userOption = input("Do you want to try again? 😈\nPress 'Enter' to start or Type 'q' to exit: ")
      print(cutPrint)
      if userOption.lower() == 'q':
        startGame = False
    else:
      print("Sorry! You lose! 😢")
      print(cutPrint)
      userOption = input("Do you want to try again? 😈\nPress 'Enter' to start or Type 'q' to exit: ")
      print(cutPrint)
      if userOption.lower() == 'q':
        startGame = False