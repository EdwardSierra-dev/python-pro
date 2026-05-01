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

  if module_selection == "3":
    is_menu_active = False
  
  elif select_module(module_selection) == "1":
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
        product_name = input("Enter the name of product: ").upper()
        product_price = int(input("Enter the price: "))
        product_stock = int(input("Enter the stock of product: "))
        product_status = True

        create_product(product_name, product_price, product_stock, product_status)

      elif inventory_module_selection == "2":
        get_products()

      elif inventory_module_selection == "3":
        product_name = input("Enter the name of product: ").upper()
        get_product_by_name(product_name)

      elif inventory_module_selection == "4":
        product_selected = input("Enter the name product to update: ").upper()
        get_product_by_name(product_selected)
        new_price = int(input("New Price: "))
        new_stock = int(input("New Stock: "))

        update_product(product_selected, new_price, new_stock)

      elif inventory_module_selection == "5":
        product_selected = input("What product do you want to delete? ").upper()
        product_to_delete = get_product_by_name(product_selected)
        delete_product(product_to_delete)

      else:
        print("Please, Enter a valid option")

  elif select_module(module_selection) == "2":
    print("We are working in sales module!! Coming soon!")

          