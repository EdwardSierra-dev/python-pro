# Functions
def is_field_empty(data):
  if data == "":
    return False
  else:
    return True

# Classes
class Contact:
  def __init__(self, id, name, phone_number, email):
    self.id = id
    self.name = name
    self.phone_number = phone_number
    self.email = email

# Vars
contact_list = []
user_choice = ""
increment = 0
name_to_search = ""

while True:

  print("Select the option ")
  print("1. Add contact")
  print("2. View contacts")
  print("3. Search contact")
  print("4. Delete contact")
  print("5. Exit: ")

  user_choice = input("Please, select an option (1-5): ")

  if user_choice == "5" : break
  
  if user_choice == "1":
    increment += 1
    contact_name = input("Enter contact name: ")
    contact_phone = input("Enter contact phone: ")
    contact_email = input("Enter contact email: ")
    if is_field_empty(contact_name) == False or is_field_empty(contact_phone) == False:
      print("The fields: name and phone cannot be empty")
    else:
      id = increment
      name = contact_name.lower()
      phone = contact_phone
      email = contact_email.lower()
      contact = Contact(id, name, phone, email)
      contact_list.append(contact)
      print("The contact was registered!")

  elif user_choice == "2":
    if len(contact_list) == 0:
      print("No contacts found!")
    else:
      for contact in contact_list:
        print(f"{contact.name} - {contact.phone_number} - {contact.email}")

  elif user_choice == "3":
    name_to_search = input(("Enter contact name: "))
    if name_to_search == "":
      print("Enter a contact name, Please!")
    else:
      if len(contact_list) == 0:
        print("The list doesn't have contacts")
      else:
        for contact in contact_list:
          if name_to_search == contact.name:
            print(f"{contact.name} - {contact.phone_number} - {contact.email}")
          else:
            print("This contact doesn't exist!")  

  elif user_choice == "4":
    name_to_search = input(("Enter contact name: "))
    if name_to_search == "":
      print("Enter a contact name, Please!")
    else:
      if len(contact_list) == 0:
        print("The list doesn't have contacts")
      else:
        for contact in contact_list:
          if name_to_search == contact.name:
            print("Eliminaste esa mondá")
          else:
            print("This contact doesn't exist!")

  else:
    print("Please enter a valid option!")