"""User → main → services → storage → data.json"""
from models import Product

# Vars
product_list = []

# CRUD
def create_product(id, name, quantity, price, is_active):
  product = Product(id, name, quantity, price, is_active)
  product_list.append(product)
  return product_list

def get_products(product_list):
  if len(product_list) == 0:
    return print("Inventory is empty")
  else:
    for product in product_list:
      return print(f"{product.name} - {product.price} - {product.quantity}")

def get_product(product_list, product_name):
  if len(product_list) == 0:
    return print("Inventory is empty")
  else:
    for product in product_list:
      if product_name == product.name:
        return print(f" Product found! \n{product.name} - {product.price} - {product.quantity}")
      else:
        return print("Product not found!")

def update_product_info(product_list, product_name):
  if len(product_list) == 0:
    return print("Inventory is empty")
  else:
    for product in product_list:
      if product_name == product.name:
        new_name = input(f"Enter the new name for {product.name}: ")
        new_price = float(input(f"Enter the new price for {product.name} Antes {product.price}: "))
        product.name = new_name
        product.price = new_price
        return print(f"The product was update!")
      else:
        return print("Product not found!")

def delete_product():
  return print("Eliminaste un producto")

def update_stock_by_product():
  return print("Agregaste un producto")

#def create_id(self):
#  return self.id + 1

def set_product_status():
  return print("Status was updated!")