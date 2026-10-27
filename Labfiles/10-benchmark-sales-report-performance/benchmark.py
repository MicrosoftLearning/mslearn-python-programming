# Import modules
import cProfile
import timeit


# Define report functions
def make_order_ids(count):
    """Return a list of order IDs. IDs 0, 1, and 2 appear twice."""
    return list(range(count)) + [0, 1, 2]


def calculate_total(sales_amounts):
    """Return the total of the sales amounts."""
    return sum(sales_amounts)


def find_duplicate_orders_slow(order_ids):
    """Return the order IDs that appear more than once by comparing every pair."""
    duplicates = []
    for i in range(len(order_ids)):
        for j in range(i + 1, len(order_ids)):
            if order_ids[i] == order_ids[j] and order_ids[i] not in duplicates:
                duplicates.append(order_ids[i])
    return duplicates


def find_duplicate_orders_fast(order_ids):
    """Return the order IDs that appear more than once by checking each ID once."""
    seen = set()
    duplicates = []
    for order_id in order_ids:
        if order_id in seen and order_id not in duplicates:
            duplicates.append(order_id)
        seen.add(order_id)
    return duplicates


def build_report(order_ids, sales_amounts):
    """Return a text report with the sales total and the duplicate order IDs."""
    total = calculate_total(sales_amounts)
    # Use the faster function to find the duplicate order IDs
    duplicates = find_duplicate_orders_slow(order_ids)
    return (
        f"Orders: {len(order_ids)}\n"
        f"Total sales: ${total:,.2f}\n"
        f"Duplicate order IDs: {duplicates}"
    )


# Test and measure
if __name__ == "__main__":
    order_ids = make_order_ids(5000)
    sales_amounts = [25.0] * len(order_ids)

    print(build_report(order_ids, sales_amounts))

    # Time three runs of the whole report and print the average per run

    # Profile the whole report and sort the results by time spent in each function

    # Time both duplicate finders at three data sizes and print the results
