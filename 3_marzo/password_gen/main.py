# Dicts
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Vars
passwordLen = int(input("How long do you want the password to be? "))
passwordParams = ""
password = ""

includeUppercase = input("Include uppercase letters (y/n): ").lower()
includeLowercase = input("Include lowercase letters (y/n): ").lower()
includeNumbers = input("Include numbers (y/n): ").lower()
includeSymbols = input("Include symbols (y/n): ").lower()

if includeUppercase == "n" and includeLowercase == "n" and includeNumbers == "n" and includeSymbols == "n":
  print("Error: You must select at least one character type.")
else:
  if includeUppercase == "y" : passwordParams += lowercase
  if includeLowercase == "y" : passwordParams += uppercase
  if includeNumbers == "y" : passwordParams += numbers
  if includeSymbols == "y" : passwordParams += symbols

print(passwordParams)


#for key in CHARACTER_SETS:
#  print(CHARACTER_SETS[key])

# SE DEBE REALIZAR LA VALIDACION DE CADA DICT KEY->VALUE PARA CONCATENARLO EN UN SET UNICO Y VALIDO
# QUE VAYA ACORDE A LA SECCIÓN DEL USUARIO.

