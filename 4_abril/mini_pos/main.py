from services import *
from models import *

# Vars

is_menu_active = True

while is_menu_active:
  print("Welcome!")
  print("What do you want to do ... ?")
  module_selection = input("1. Enter inventory module\n" \
                          "2. Enter sale module\n" \
                          "3. Exit\n" \
                          "Type 1-3 and press 'Enter': ")
  
  print("-" * 50)

  if select_module(module_selection) == "1":
    is_user_in_inventory = True
    while is_user_in_inventory:
      print("You had joined in inventory module!")
      inventory_module_selection = input("1. Create product\n" \
                            "2. Get products list\n" \
                            "3. Look for a product by name\n" \
                            "4. Update product (Name, Price or Stock)\n" \
                            "5. Delete product by name\n" \
                            "6. Exit\n" \
                            "Type 1-6 and press 'Enter': \n")
      
      if inventory_module_selection == "6":
        is_user_in_inventory = False
      
      elif inventory_module_selection == "1":
        product_name = input("Enter de name of product: ").upper()
        product_price = int(input("Enter the price: "))
        product_stock = int(input("Enter the stock of product: "))
        product_status = True

        create_product(product_name, product_price, product_stock, product_status)

      elif inventory_module_selection == "2":
        get_products()

      else:
        print("Please, Enter a valid option")

  elif module_selection == "3":
    is_menu_active = False