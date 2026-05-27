# Imports
from time import gmtime, strftime
from models import *
from storage import product_list

# Vars
order_date = strftime("%d %b %Y %H:%M", gmtime())

def create_product():
  product_name = input("Enter name of product: ").split()
  product_price = int(input("Enter price of product: "))

  food = Food(product_name, product_price)
  product_list.append(food)
  print("The product was created")

def create_order(customer_name, products, address, city, phone_number, qty):
  new_order = Order()

  return new_order
