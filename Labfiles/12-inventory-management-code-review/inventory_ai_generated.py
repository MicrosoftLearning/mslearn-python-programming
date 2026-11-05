# AI-generated inventory code. It looks reasonable, but it has bugs.
# Keep the function names, the parameters, and the INVENTORY name.
# check_inventory.py calls them.

# Mock data. The AI assumed a database, but this exercise uses a dictionary.
INVENTORY = {
    'WIDGET-A': {'warehouse1': 50, 'warehouse2': 30},
    'WIDGET-B': {'warehouse1': 0, 'warehouse2': 100},
    'WIDGET-C': {'warehouse1': 75, 'warehouse2': 25},
}


# Issue 1: Fix hallucinated functions
def get_stock_level(product_id, warehouse_id):
    """Return the stock level for one product in one warehouse."""
    return fetch_inventory(product_id, warehouse_id)


# Issue 2: Add error handling
def update_stock(product_id, warehouse_id, quantity_change):
    """Add stock (positive change) or remove stock (negative change). Return the new level."""
    return update_inventory_sync(product_id, warehouse_id, quantity_change)


# Issue 3: Fix validation gaps
def transfer_stock(product_id, from_warehouse, to_warehouse, quantity):
    """Move stock between warehouses. Return the new levels as (from_level, to_level)."""
    INVENTORY[product_id][from_warehouse] -= quantity
    INVENTORY[product_id][to_warehouse] += quantity
    return INVENTORY[product_id][from_warehouse], INVENTORY[product_id][to_warehouse]


if __name__ == "__main__":
    print(get_stock_level('WIDGET-A', 'warehouse1'))
