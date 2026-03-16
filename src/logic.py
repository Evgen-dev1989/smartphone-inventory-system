from src.models import Warehouse, Smartphone


warhause = Warehouse()
# apple = Smartphone(brand = 'Apple', model = '15_Pro' ,price = 500, quantity = 7)
# xiaomi = Smartphone(brand = 'Xiaomi', model = 'Redmi Note 14', price = 221, quantity = 5)
# samsung = Smartphone(brand = 'Samsung', model = 'Galaxy ', price = 433, quantity = 4)
# nokia = Smartphone(brand = 'Nokia', model = 'Charcoal', price = 200, quantity = 0)


# warhause.add_product(apple)
# warhause.add_product(xiaomi)
# warhause.add_product(samsung)
# warhause.add_product(nokia)

def sell_item():
    pass

def get_inventory_report(warhause):
    return sum(phone.quantity  for phone in warhause.items)

print(get_inventory_report(warhause))

def get_total_stock(warhause):
    return sum(phone.price * phone.quantity  for phone in warhause.items)

def find_out_of_stock(warhause):
    return [phone.brand for phone in warhause.items if phone.quantity == 0]

def apply_global_discount(warhause, percent):
    result = []
    for phone in warhause.items:
        new_price = round(phone.price * (1 - percent / 100), 2)
        result.append((phone.brand, new_price))
    return result
