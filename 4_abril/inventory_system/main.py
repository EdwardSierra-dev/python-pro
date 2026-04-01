# Vars
menu_activated = True
user_selection = ""

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
