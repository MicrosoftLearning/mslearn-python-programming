# Checks the inventory functions against expected results. Don't edit this file.
import copy
import inventory_ai_generated as inventory

BASE_INVENTORY = {
    'WIDGET-A': {'warehouse1': 50, 'warehouse2': 30},
    'WIDGET-B': {'warehouse1': 0, 'warehouse2': 100},
    'WIDGET-C': {'warehouse1': 75, 'warehouse2': 25},
}

# Each check is (function name, arguments, expected result).
# The expected result "error" means the function should raise a ValueError
# and leave the inventory unchanged.
checks = [
    ("get_stock_level", ("WIDGET-A", "warehouse1"), 50),
    ("get_stock_level", ("WIDGET-B", "warehouse2"), 100),
    ("get_stock_level", ("INVALID", "warehouse1"), "error"),
    ("get_stock_level", ("WIDGET-A", "warehouse9"), "error"),
    ("update_stock", ("WIDGET-A", "warehouse1", 10), 60),
    ("update_stock", ("WIDGET-A", "warehouse1", -50), 0),
    ("update_stock", ("WIDGET-A", "warehouse1", -51), "error"),
    ("update_stock", ("WIDGET-A", "warehouse1", 0), "error"),
    ("update_stock", ("INVALID", "warehouse1", 5), "error"),
    ("update_stock", ("WIDGET-A", "warehouse9", 5), "error"),
    ("transfer_stock", ("WIDGET-B", "warehouse2", "warehouse1", 50), (50, 50)),
    ("transfer_stock", ("WIDGET-B", "warehouse1", "warehouse1", 10), "error"),
    ("transfer_stock", ("WIDGET-A", "warehouse1", "warehouse2", 10000), "error"),
    ("transfer_stock", ("WIDGET-A", "warehouse1", "warehouse2", 0), "error"),
    ("transfer_stock", ("WIDGET-A", "warehouse1", "warehouse9", 5), "error"),
    ("transfer_stock", ("INVALID", "warehouse1", "warehouse2", 5), "error"),
]

for function_name, args, expected in checks:
    # Start each check from the same inventory.
    inventory.INVENTORY = copy.deepcopy(BASE_INVENTORY)
    before = copy.deepcopy(inventory.INVENTORY)
    try:
        result = getattr(inventory, function_name)(*args)
    except ValueError:
        result = "error"
    except Exception as ex:
        result = type(ex).__name__

    if expected == "error":
        unchanged = inventory.INVENTORY == before
        status = "PASS" if result == "error" and unchanged else "FAIL"
    else:
        status = "PASS" if result == expected else "FAIL"

    call = f"{function_name}{args!r}"
    print(f"{status}  {call:<62} -> {str(result):<12} expected {expected}")
