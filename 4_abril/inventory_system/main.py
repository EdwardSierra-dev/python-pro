"""User → main → services → storage → data.json"""

# Imports
from services import add_product
from models import Product

# Vars
menu_activated = True
user_selection = ""
product_id = 0
product_name = ""
product_qty = 0
product_price = 0
product_status = True

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
		product_name = input("Enter product name: ")

		if product_name == "" or product_name == " ":
			print("Cannot create product whitout name!, Try again")
		else:
			product_qty = int(input("How much ...? "))
			if product_qty < 0:
				print("Cannot create product with negative stock")
			else:
				product_price = int(input("Price ...? "))
				if product_price > 0:
					product_status = True
					product_id = "1"
					check_product_data = input(f"Product name: {product_name}\n" \
											f"Product quantity: {product_qty}\n" \
											f"Product price: {product_price}\n" \
											"Is this correct? (y/n): ")
					if check_product_data == "y":
						temp_product = Product(product_id, product_name, product_qty, product_price, product_status)
						print(f"New product added {temp_product.name}!")
						add_product()
					else:
						print("Product creation cancelled")
				else:
					print("Cannot create product with price 0")

	elif user_selection == "2":
		print("List of products")