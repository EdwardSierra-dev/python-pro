# Imports

# Vars
is_menu_active = True
user_select = 0
product_name = ""
product_price = 0



print("Welcome 5G Test")
print("------------------------------")

while is_menu_active == True:
  user_select = int(input("1. Create product\n 2. Take order\n"))
  if user_select == 1:
    print("Welcome to inventory module")

  elif user_select == 2:
    print("Welcome to orders module")
    



  print("Estamos en el menú")