# Imports
from time import gmtime, strftime
from models import *
from storage import *

print (strftime("%d %b %Y %H:%M", gmtime()))

def create_product():
  product_name = input("Enter name of product: ").split()
  product_price = int(input("Enter price of product: ").split())

  food = Food(product_name, product_price)
  product_list.append(food)

def create_order(customer_name, products, address, city, phone_number):
  new_order = Order()

  return new_order
