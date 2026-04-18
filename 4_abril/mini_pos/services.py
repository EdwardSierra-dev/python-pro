from models import Product

# Vars

product_list = []

# Functions

def gen_id():
  id_list = []
  id = 1
  id_list.append(id)

  for i in range (len(id_list)):
    id += i

  return id

def select_module(module_selection):
  if module_selection == "1":
    print("Welcome to the inventory module!")
  elif module_selection == "2":
    print("Welcome to the sale module!")

  return module_selection

def create_product(name, price, stock, status):
  if name == "" or name == " ":
    print("The name cannot be empty!")
    raise

  if price < 0:
    print("The price cannot be zero!")
    raise

  if stock <= 0:
    print("The stock cannot be negative")
    raise

  id = gen_id()
  new_product = Product(id, name, price, stock, status)
  product_list.append(new_product)

  return print("The product was created!")

def get_products():
  if len(product_list) == 0:
    print("The inventory is empty")
  else:
    for product in product_list:
      if product.status == True:
        print(f"{product.name}")
