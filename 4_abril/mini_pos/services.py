# Functions

def gen_id():
  id_list = []
  id = 1
  id_list.append(id)

  for i in len(id_list):
    id += i

  return id

def select_module(module_selection):
  if module_selection == "1":
    print("Welcome to the inventory module!")
  elif module_selection == "2":
    print("Welcome to the sale module!")
  else:
    print("Please, Enter 1 o 2")

  return module_selection