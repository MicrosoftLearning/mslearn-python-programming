# Parse one row of sales data
def parse_sales_row(line: str) -> float:
    """Return the sale amount from one CSV row.

    Raises ValueError if the row has no amount, the amount isn't a number,
    or the amount isn't greater than zero.
    """
    columns = line.strip().split(",")
    if len(columns) < 3:
        raise ValueError("row is missing the amount")
    amount = float(columns[2])
    if amount <= 0:
        raise ValueError("amount must be greater than zero")
    return amount


# Read sales data from CSV file
def rd(filename):
    sales_amounts = []
    with open(filename) as file:
        next(file)  # Skip the header row
        for line_number, line in enumerate(file, start=2):
            # Skip a row that parse_sales_row rejects and print its line number
            sales_amounts.append(parse_sales_row(line))
    return sales_amounts


# Calculate statistics
# Add type hints and a docstring that describes the ValueError
def avg(sales_amounts):
    # Raise a ValueError if the list of sales amounts is empty
    return sum(sales_amounts) / len(sales_amounts)


# Display report
def display_sales_report(sales_amounts):
    print("Sales Report")
    print("=" * 40)

    if len(sales_amounts) == 0:
        print("No valid sales data found.")
        return

    print(f"Total Sales:        ${sum(sales_amounts):,.2f}")
    print(f"Average Sale:       ${avg(sales_amounts):,.2f}")
    print(f"Highest Sale:       ${max(sales_amounts):,.2f}")
    print(f"Lowest Sale:        ${min(sales_amounts):,.2f}")
    print(f"Number of Sales:    {len(sales_amounts)}")
    print("=" * 40)


# Main program flow
if __name__ == "__main__":
    filename = "sales.csv"
    print(f"Reading sales from {filename}...")
    # If the file isn't found, print an error message and use an empty list
    sales_amounts = rd(filename)
    display_sales_report(sales_amounts)
