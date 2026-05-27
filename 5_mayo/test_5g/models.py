class Food:
  def __init__(self, name, price):
    if not name:
      raise ValueError("Name cannot be empty")

    if price <= 0:
      raise ValueError("Price must be grater than 0")

    self.name = name
    self.price = price

    pass

class Order:
  def __init__(self,id, status, customer_name, products, total, address, city, phone, order_date, qty):

    self.status = status
    self.customer_name = customer_name
    self.products = products
    self.total = total
    self.address = address
    self.city = city
    self.phone = phone
    self.id = id
    self.order_date = order_date
    self.qty = qty

    pass