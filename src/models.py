class Smartphone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, smartphone):
        self.items.append(smartphone)