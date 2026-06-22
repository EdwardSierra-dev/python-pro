# Imports
from time import gmtime, strftime
from models import *
from storage import product_list, product_in_order

# Vars
order_date = strftime("%d %b %Y %H:%M", gmtime())
