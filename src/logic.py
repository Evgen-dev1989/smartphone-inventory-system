from models import Warehouse, Smartphone


warhause = Warehouse()
iphone_15 = Smartphone(brand = 'Iphone',model = 15 ,price = '500$',quantity = 7)
iphone_14_pro = Smartphone(brand = 'Iphone',model = '14 pro' ,price = '350$', quantity = 3)


warhause.add_product(iphone_15)


def sell_item():
    pass

def get_inventory_report():
    arr = warhause.items

print(warhause.items)