# Checks calculate_shipping against example orders. Don't edit this file.
from shipping import calculate_shipping

# Each example is (weight_kg, order_total, expected result).
# The expected result "error" means the function should raise a ValueError.
examples = [
    (0.5, 20.00, 5.00),
    (3, 20.00, 10.00),
    (8, 20.00, 20.00),
    (3, 60.00, 0.00),
    (1, 20.00, 10.00),
    (5, 20.00, 10.00),
    (3, 50.00, 10.00),
    (0, 20.00, "error"),
    (-2, 20.00, "error"),
    (3, -10.00, "error"),
    ("heavy", 20.00, "error"),
]

for weight_kg, order_total, expected in examples:
    try:
        result = calculate_shipping(weight_kg, order_total)
    except ValueError:
        result = "error"
    except Exception as ex:
        result = type(ex).__name__

    status = "PASS" if result == expected else "FAIL"
    call = f"calculate_shipping({weight_kg!r}, {order_total})"
    print(f"{status}  {call:<36} -> {str(result):<10} expected {expected}")
