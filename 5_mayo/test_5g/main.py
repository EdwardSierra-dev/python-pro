# Imports
from services import *
from storage import *

# Vars
is_menu_active = True
user_select = 0
product_name = ""
product_price = 0
customer_name = ""
product_in_order = []
customer_address = ""
city = ""
customer_phone = ""
how_much_products = 0

print("Welcome 5G Test")
print("------------------------------")

while is_menu_active == True:
  user_select = int(input("1. Create product\n 2. Take order\n 3. Exit: "))
  if user_select == 1:
    print("Welcome to inventory module")
    create_product() 

  elif user_select == 2:
    print("Welcome to orders module")
    customer_name = input("Enter the customer name: ").split()
    customer_address = input("Enter the customer address: ")
    city = input("Enter the city: ").split()
    customer_phone = input("Enter the customer phone").split()
    how_much_products = int(input("How much products the customer wants? "))
    product_in_order = [how_much_products]

    create_order(customer_name, product_in_order, customer_address, city, customer_phone, product_in_order)
    

  elif user_select == 3:
    is_menu_active = False

  print("Estamos en el menú")