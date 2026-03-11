# Imports
import pyperclip
from random import randrange

# Dicts
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Vars
numberOfPasswords = int(input("How many passwords do you want to generate? "))

for i in range(numberOfPasswords):
  passwordLen = int(input("How long do you want the password to be? "))
  passwordParams = ""
  password = ""

  # Set password params
  includeUppercase = input("Include uppercase letters (y/n): ").lower()
  includeLowercase = input("Include lowercase letters (y/n): ").lower()
  includeNumbers = input("Include numbers (y/n): ").lower()
  includeSymbols = input("Include symbols (y/n): ").lower()

  # Validate the params selected and set the params accepted
  if includeUppercase == "n" and includeLowercase == "n" and includeNumbers == "n" and includeSymbols == "n":
    print("Error: You must select at least one character type.")
  else:
    if includeUppercase == "y" : passwordParams += lowercase
    if includeLowercase == "y" : passwordParams += uppercase
    if includeNumbers == "y" : passwordParams += numbers
    if includeSymbols == "y" : passwordParams += symbols

    for j in range(passwordLen):
      password += passwordParams[randrange(0, len(passwordParams), 1)]

  print(f"Su contraseña {i + 1} es: {password}")
  pyperclip.copy(password)
  print("Password was copied in you clipboard!")