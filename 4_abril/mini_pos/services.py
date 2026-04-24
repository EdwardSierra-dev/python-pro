from models import Product

# Vars

product_list = []
id_list = []

# Functions

def gen_id():
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
  else:
    print("Please, Enter 1 o 2")

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
        print(f"{product.id} - {product.name} - {product.stock} - {product.price} - {product.status}")

"""Se debe mejorar la lógica de get_product_by_name
Se está comparando cada objeto mas no buscando
"""

def get_product_by_name(name):
  if len(product_list) == 0:
    print("The inventory is empty")
  else:
    for product in product_list:
      if product.name != name:
        print(f"{product.id} - {product.name} - {product.stock} - {product.price}")
  return product

def update_product(name, price, stock):
  for product in product_list:
    if name.upper().strip() == product.name.upper().strip():
      product.name = name
      product.price = price
      product.stock = stock
  print("The product was updated!")

def delete_product(product: Product):
  product.status = False
  print(f"The product {product.name} was deleted!")