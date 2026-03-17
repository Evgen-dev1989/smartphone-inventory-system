# Smartphone Inventory System

## Description
This project is designed to manage a smartphone warehouse. The system allows you to store information about smartphone models, their quantity, price, and perform basic operations: adding products, getting warehouse reports, searching for models, applying discounts, and identifying out-of-stock models.

## Project Structure

- `src/models.py` — contains classes:
	- `Smartphone`: smartphone model (brand, model, price, quantity)
	- `Warehouse`: warehouse, supports adding smartphones and searching by model
- `src/logic.py` — implements business logic:
	- Counting the total number of smartphones
	- Calculating the total warehouse value
	- Finding out-of-stock models
	- Applying a global discount
- `tests/test_logic.py` — tests for warehouse and smartphone logic

## Quick Start

1. Clone the repository and navigate to the project folder.
2. (Recommended) Create and activate a virtual environment:
	 ```powershell
	 python -m venv .venv
	 .venv\Scripts\Activate.ps1
	 ```
3. Install dependencies (if any):
	 ```powershell
	 pip install -r requirements.txt
	 ```

## Usage

Example of creating a warehouse and adding smartphones:

```python
from src.models import Warehouse, Smartphone
from src.logic import get_inventory_report

warehouse = Warehouse()
iphone = Smartphone('Apple', '15_Pro', 500, 7)
warehouse.add_product(iphone)
print(get_inventory_report(warehouse))
```

## Testing

To run the tests, use:
```powershell
pytest
```

## Features
- Add smartphones to the warehouse
- Get reports on quantity and value
- Find out-of-stock models
- Apply a global discount

## Requirements
- Python 3.8+
- pytest (for testing)


