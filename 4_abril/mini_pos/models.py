class Product:
	def __init__(self, id, name, price, stock, status):
		if not name:
			raise ValueError("Name cannot be empty")

		if stock < 0:
			raise ValueError("Stock cannot be negative")

		if price <= 0:
			raise ValueError("Price must be greater than 0")
		
		self.id = id
		self.name = name
		self.price = price
		self.stock = stock
		self.status = status

class Sale:
	def __init__(self, id, products, total):

		if total < 0:
			raise ValueError("The sale never must be negative")

		self.id = id
		self.products = products

		pass