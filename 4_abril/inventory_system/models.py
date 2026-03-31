class Product:
    def __init__(self, id: int, name: str, quantity: int, price: float):
        if not name:
            raise ValueError("Name cannot be empty")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price