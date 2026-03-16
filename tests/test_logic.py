import pytest
from src.models import Smartphone, Warehouse
from src.logic import apply_global_discount, find_out_of_stock, get_total_stock, get_inventory_report

apple = Smartphone(brand = 'Apple', model = '15_Pro',price = 500, quantity = 7)
xiaomi = Smartphone(brand = 'Xiaomi', model = 'Redmi_Note_14', price = 221, quantity = 5)
samsung = Smartphone(brand = 'Samsung', model = 'Galaxy', price = 433, quantity = 4)
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


def test_get_inventory_report(filled_warehouse):
    assert get_inventory_report(filled_warehouse) == 16

def test_find_out_of_stock(filled_warehouse):
    assert find_out_of_stock (filled_warehouse) == ['Nokia']




@pytest.mark.parametrize("percent, expected", [
    (6, [('Apple', 470.0), ('Xiaomi', 207.74), ('Samsung', 407.02), ('Nokia', 188.0)]),
    (10, [('Apple', 450.0), ('Xiaomi', 198.9), ('Samsung', 389.7), ('Nokia', 180.0)]),
])
def test_apply_global_discount(filled_warehouse, percent, expected):
    result = apply_global_discount(filled_warehouse, percent)
    assert result == expected



