class Smartphone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.brand} {self.model} ({self.price})"
    

class Warehouse:
    def __init__(self):
        self.items = []
    
    def add_product(self, phone):
        if isinstance(phone, Smartphone):
            self.items.append(phone)
        else:
            raise ValueError('You can only add objects Smartphone')
        
    def find_model(self, model_name):
        for phone in self.items:
            if phone.model == model_name:
                return phone
        return None