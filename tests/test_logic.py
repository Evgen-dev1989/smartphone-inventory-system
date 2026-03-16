import pytest
from src.models import Smartphone, Warehouse
from src.logic import apply_global_discount, find_out_of_stock, get_total_stock, get_inventory_report


apple = Smartphone(brand = 'Apple', model = 15 ,price = 500, quantity = 7)
xiaomi = Smartphone(brand = 'Xiaomi', model = 'Redmi Note 14', price = 221, quantity = 5)
samsung = Smartphone(brand = 'Samsung', model = 'Galaxy ', price = 433, quantity = 4)
nokia = Smartphone(brand = 'Nokia', model = 'Charcoal', price = 200, quantity = 0)


@pytest.fixture
def filled_warehouse():
    w = Warehouse()
    w.add_product(apple) 
    w.add_product(xiaomi)     
    w.add_product(samsung)     
    w.add_product(nokia)     
    return w

def test_total_stock_value(filled_warehouse):
    assert get_total_stock(filled_warehouse) == 6337

