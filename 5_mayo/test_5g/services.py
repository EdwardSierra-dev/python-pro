# Imports
from models import *
from storage import *

def create_product():
  product_name = input("Enter name of product: ").split()
  product_price = int(input("Enter price of product: ").split())

  food = Food(product_name, product_price)
  product_list.append(food)