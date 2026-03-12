from models import Warehouse, Smartphone


warhause = Warehouse()
iphone_15 = Smartphone(brand = 'iphone', model = 15 ,price = '500$',quantity = 7)
iphone_14_pro = Smartphone(brand = 'iphone',model = '14 pro' ,price = '350$', quantity = 3)
xiaomi = Smartphone(brand = 'xiaomi', model = 'Redmi Note 14', price = '221$',quantity = 5)
samsung = Smartphone(brand = 'samsung', model = 'Galaxy ', price = '433$', quantity = 4)


warhause.add_product(iphone_15)
warhause.add_product(iphone_14_pro)
warhause.add_product(xiaomi)
warhause.add_product(samsung)
def sell_item():
    pass

def get_inventory_report():
    arr = warhause.items

for i in warhause.items:
    print(i)