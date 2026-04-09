from services import *

# Vars

is_menu_active = True

while is_menu_active:
  print("Welcome!")
  print("What do you want to do ... ?")
  module_selection = input("1. Enter inventory module\n" \
                          "2. Enter sale module\n" \
                          "Type 1 or 2 and press 'Enter': ")
  
  print("-" * 50)

  select_module(module_selection)