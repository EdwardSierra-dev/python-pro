"""User → main → services → storage → data.json"""

# Imports
from services import create_product, get_products, get_product, update_product_info

# Vars
menu_activated = True
user_selection = ""
product_id = 0
product_name = ""
product_qty = 0
product_price = 0
product_status = True
set_list = []

while menu_activated:
	print("Welcome to the storage app!")
	print("What would you like to do?")
	print("1. Add a product\n" \
				"2. List products\n" \
				"3. Search a product\n" \
				"4. Update a product\n" \
				"5. Delete a product\n" \
				"6. Increase stock\n" \
				"7. Decrease stock\n" \
				"8. Exit")
	user_selection = input("Select 1-8: ")

	if user_selection == "8" : menu_activated = False

	if user_selection == "1":
		product_name = input("Enter product name: ").upper()

		if product_name == "" or product_name == " ":
			print("Cannot create product whitout name!, Try again")
		else:
			product_qty = int(input("How much ...? "))
			if product_qty < 0:
				print("Cannot create product with negative stock")
			else:
				product_price = int(input("Price ...? "))
				if product_price > 0:
					product_is_active = True
					check_product_data = input(f"Product name: {product_name.upper()}\n" \
											f"Product quantity: {product_qty}\n" \
											f"Product price: {product_price}\n" \
											"Is this correct? (y/n): ")
					if check_product_data == "y":
						set_list = create_product(1, product_name, product_qty, product_price, product_is_active)
						print(f"New Product Added {product_name}!")
					else:
						print("Product creation cancelled")
				else:
					print("Cannot create product with price 0")

	elif user_selection == "2":
		get_products(set_list)

	elif user_selection == "3":
		product_name_to_search = input("Enter the name: ").upper()
		get_product(set_list, product_name_to_search)

	elif user_selection == "4":
		product_name_to_search = input("Enter the name: ").upper()
		update_product_info(set_list, product_name_to_search)