# Dicts
CHARACTER_SETS = {
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers": "0123456789",
    "symbols": "!@#$%^&*()"
}

# Vars
passwordLen = int(input("How long do you want the password to be?"))
password = ""

includeUppercase = input("Include uppercase letters (y/n)")
includeLowercase = input("Include lowercase letters (y/n)")
includeNumbers = input("Include numbers (y/n)")
includeSymbols = input("Include symbols (y/n)")

if includeUppercase == "n" and includeLowercase == "n" and includeNumbers == "n" and includeSymbols == "n":
  print("Error: You must select at least one character type.")
else:
  for i in range(passwordLen):
    for key in CHARACTER_SETS:
      print(CHARACTER_SETS[key])

# SE DEBE REALIZAR LA VALIDACION DE CADA DICT KEY->VALUE PARA CONCATENARLO EN UN SET UNICO Y VALIDO
# QUE VAYA ACORDE A LA SECCIÓN DEL USUARIO.

