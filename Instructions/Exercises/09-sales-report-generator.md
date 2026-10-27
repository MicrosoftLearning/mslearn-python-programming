---
lab:
    title: 'Build a sales report generator with error handling'
    description: 'Create a Python program that reads sales data from a CSV file, handles errors gracefully, calculates statistics, and generates a formatted report.'
    level: 200
    duration: 35
    islab: true
    status: 'released'
---

# Build a sales report generator with error handling

In this exercise, you build a sales report generator that reads sales data from a CSV file, handles errors gracefully, and prints a formatted report. You practice reading files, catching errors with `try` and `except`, and organizing your code into **functions**.

This exercise takes approximately **35** minutes.

## Set up your workspace

You'll write and run your code in Visual Studio Code. The starter code for this exercise lives in a GitHub repository — you'll clone that repo now if you haven't already.

> **Tip**: If you've already cloned the repo during another exercise, skip to the next section.

1. Open a new **Visual Studio Code** window (**File > New Window**).

1. On the Welcome page, select **Clone Git Repository...** (or open the Command Palette with **Ctrl+Shift+P** and run **Git: Clone**).

1. Paste the following URL and press **Enter**:

    ```
    https://github.com/MicrosoftLearning/mslearn-python-programming.git
    ```

1. When the file selection dialog appears, create a new folder in a convenient location to hold the repo (for example, `mslearn-python`), select it, and click **Select as Repository Destination**.

1. After the clone completes, select **Open** to open the folder in VS Code.

## Review the starter code

1. In the VS Code file explorer, navigate to the `Labfiles/09-sales-report-generator` subfolder.

1. Select the `sales_report.py` file. You'll see a set of guiding comments that act as an outline for your program — each one marks where a specific piece of code belongs:

    ```python
    # Read sales data from CSV file

    # Calculate statistics

    # Display report

    # Main program flow
    ```

    Remember, comments are ignored by Python when the program runs. They're just there to help you organize your code. In the steps that follow, you'll add code beneath each comment.

1. Select the `sales.csv` file. It contains a header row followed by sample sales records:

    ```text
    Date,Product,Amount
    2024-01-15,Widget A,1500.00
    2024-01-15,Widget B,2100.00
    2024-01-15,Widget C,INVALID
    2024-01-16,Widget A,1200.00
    2024-01-16,Widget B
    2024-01-17,Widget C,450.00
    ```

    Some of the records are intentionally bad: line 4 has `INVALID` instead of an amount, and line 6 is missing its amount. Real-world data is often messy like this, so your program needs to handle it without crashing.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

1. Open a terminal (**Terminal > New Terminal**) and change to the exercise folder so your program can find `sales.csv`:

    ```bash
    cd Labfiles/09-sales-report-generator
    ```

    You'll run your program from this terminal throughout the exercise.

## Handle a missing file

A report generator is only useful if it can read its data. You'll start with a function that opens the file and reads the amount from each row. First, you'll make sure the program doesn't crash if the file doesn't exist.

1. Beneath the `# Read sales data from CSV file` comment, add the following:

    ```python
    def read_sales_data(filename):
        sales_amounts = []
        try:
            with open(filename, "r") as file:
                next(file)  # Skip the header row
                for line in file:
                    columns = line.strip().split(",")
                    amount = float(columns[2])
                    sales_amounts.append(amount)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")

        return sales_amounts
    ```

    - `with open()` opens the file and closes it automatically when the block ends.
    - `next(file)` skips the header row (`Date,Product,Amount`).
    - `line.strip().split(",")` turns a line of text into a list of columns. The amount is in the third column, at index `2`.
    - `float()` converts the amount from text to a number.
    - `except FileNotFoundError` catches the error when the file is missing and prints a friendly message instead of crashing.

1. Temporarily add the following line at the bottom of your program to test the function with a file that doesn't exist:

    ```python
    print(read_sales_data("missing.csv"))
    ```

1. Run the program from the terminal:

    ```bash
    python sales_report.py
    ```

    You should see:

    ```output
    Error: File 'missing.csv' not found
    []
    ```

1. Now change the test line to use the real data file, and run the program again:

    ```python
    print(read_sales_data("sales.csv"))
    ```

    This time the program crashes with an error that ends like this:

    ```output
    ValueError: could not convert string to float: 'INVALID'
    ```

    `float()` can't convert the word `INVALID` into a number. You'll fix that next.

## Skip bad data instead of crashing

You'll handle the bad records by catching the `ValueError` for each row, reporting the problem, and moving on to the next row. You'll also check that each row has enough columns.

1. Replace the `read_sales_data` function with the following version:

    ```python
    def read_sales_data(filename):
        sales_amounts = []
        try:
            with open(filename, "r") as file:
                next(file)  # Skip the header row
                for line_num, line in enumerate(file, start=2):
                    columns = line.strip().split(",")
                    if len(columns) < 3:
                        print(f"Line {line_num}: Missing data - skipped")
                        continue
                    try:
                        sales_amounts.append(float(columns[2]))
                    except ValueError:
                        print(f"Line {line_num}: Invalid amount - skipped")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")

        return sales_amounts
    ```

    - `enumerate(file, start=2)` numbers each line. It starts at `2` because the header was line `1`.
    - `len(columns) < 3` catches rows that are missing the amount column. `continue` skips to the next row.
    - The inner `try` / `except ValueError` catches amounts that can't be converted to a number.
    - Bad records are reported and skipped, not fatal.

1. Run the program. You should see:

    ```output
    Line 4: Invalid amount - skipped
    Line 6: Missing data - skipped
    [1500.0, 2100.0, 1200.0, 450.0]
    ```

1. Delete the temporary `print(read_sales_data("sales.csv"))` line.

## Calculate the statistics

Next, you'll add four small functions that each calculate one statistic. Each function takes the list of sales amounts and **returns** a value.

1. Beneath the `# Calculate statistics` comment, add the following:

    ```python
    def calculate_total(sales_amounts):
        return sum(sales_amounts)

    def calculate_average(sales_amounts):
        if len(sales_amounts) == 0:
            return 0
        return calculate_total(sales_amounts) / len(sales_amounts)

    def find_highest_sale(sales_amounts):
        if len(sales_amounts) == 0:
            return 0
        return max(sales_amounts)

    def find_lowest_sale(sales_amounts):
        if len(sales_amounts) == 0:
            return 0
        return min(sales_amounts)
    ```

    - Each function does one job, which keeps the code easy to read and test.
    - `calculate_average`, `find_highest_sale`, and `find_lowest_sale` check for an empty list first. Dividing by zero, or calling `max()` or `min()` on an empty list, would otherwise raise an error.
    - `calculate_average` reuses `calculate_total` instead of repeating the calculation.

## Display the report

Now you'll write a function that uses your calculation functions and prints the results in a neatly formatted report.

1. Beneath the `# Display report` comment, add the following:

    ```python
    def display_sales_report(sales_amounts):
        print("Sales Report:")
        print("=" * 40)

        if len(sales_amounts) == 0:
            print("No valid sales data found.")
            return

        total = calculate_total(sales_amounts)
        average = calculate_average(sales_amounts)
        highest = find_highest_sale(sales_amounts)
        lowest = find_lowest_sale(sales_amounts)

        print(f"Total Sales:        ${total:,.2f}")
        print(f"Average Sale:       ${average:,.2f}")
        print(f"Highest Sale:       ${highest:,.2f}")
        print(f"Lowest Sale:        ${lowest:,.2f}")
        print(f"Number of Sales:    {len(sales_amounts)}")
        print("=" * 40)
    ```

    - `"=" * 40` repeats the `=` character 40 times to draw a divider line.
    - `:,.2f` formats a number with thousands separators and two decimal places (for example, `5250.0` becomes `5,250.00`).
    - If there's no valid data, the function prints a message and returns early instead of showing a report full of zeros.

## Add the main program

The last piece ties everything together: read the data, then display the report.

1. Beneath the `# Main program flow` comment, add the following:

    ```python
    if __name__ == "__main__":
        filename = "sales.csv"
        print(f"Reading sales from {filename}...")
        sales_amounts = read_sales_data(filename)
        display_sales_report(sales_amounts)
    ```

    - `if __name__ == "__main__":` makes this code run only when you run the file directly. If another program imports your functions, this block is skipped.
    - The report is built from the list returned by `read_sales_data`, so the data flows from one function to the next.

1. Your complete program should now look like this:

    ```python
    # Read sales data from CSV file
    def read_sales_data(filename):
        sales_amounts = []
        try:
            with open(filename, "r") as file:
                next(file)  # Skip the header row
                for line_num, line in enumerate(file, start=2):
                    columns = line.strip().split(",")
                    if len(columns) < 3:
                        print(f"Line {line_num}: Missing data - skipped")
                        continue
                    try:
                        sales_amounts.append(float(columns[2]))
                    except ValueError:
                        print(f"Line {line_num}: Invalid amount - skipped")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")

        return sales_amounts

    # Calculate statistics
    def calculate_total(sales_amounts):
        return sum(sales_amounts)

    def calculate_average(sales_amounts):
        if len(sales_amounts) == 0:
            return 0
        return calculate_total(sales_amounts) / len(sales_amounts)

    def find_highest_sale(sales_amounts):
        if len(sales_amounts) == 0:
            return 0
        return max(sales_amounts)

    def find_lowest_sale(sales_amounts):
        if len(sales_amounts) == 0:
            return 0
        return min(sales_amounts)

    # Display report
    def display_sales_report(sales_amounts):
        print("Sales Report:")
        print("=" * 40)

        if len(sales_amounts) == 0:
            print("No valid sales data found.")
            return

        total = calculate_total(sales_amounts)
        average = calculate_average(sales_amounts)
        highest = find_highest_sale(sales_amounts)
        lowest = find_lowest_sale(sales_amounts)

        print(f"Total Sales:        ${total:,.2f}")
        print(f"Average Sale:       ${average:,.2f}")
        print(f"Highest Sale:       ${highest:,.2f}")
        print(f"Lowest Sale:        ${lowest:,.2f}")
        print(f"Number of Sales:    {len(sales_amounts)}")
        print("=" * 40)

    # Main program flow
    if __name__ == "__main__":
        filename = "sales.csv"
        print(f"Reading sales from {filename}...")
        sales_amounts = read_sales_data(filename)
        display_sales_report(sales_amounts)
    ```

## Run the program

1. Run the program from the terminal:

    ```bash
    python sales_report.py
    ```

1. You should see the following output:

    ```output
    Reading sales from sales.csv...
    Line 4: Invalid amount - skipped
    Line 6: Missing data - skipped
    Sales Report:
    ========================================
    Total Sales:        $5,250.00
    Average Sale:       $1,312.50
    Highest Sale:       $2,100.00
    Lowest Sale:        $450.00
    Number of Sales:    4
    ========================================
    ```

    The program skipped the two bad records, reported what was wrong with each, and calculated the statistics from the four valid sales.

1. Test the error handling for a missing file. Change `filename = "sales.csv"` to `filename = "missing.csv"` and run the program again. You should see:

    ```output
    Reading sales from missing.csv...
    Error: File 'missing.csv' not found
    Sales Report:
    ========================================
    No valid sales data found.
    ```

    Change the file name back to `sales.csv` when you're done.

## Extend with GitHub Copilot

Now that the report generator is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Reject negative amounts**

> "In my `read_sales_data` function, how can I skip any amount that is zero or negative and report it like the other bad records?"

This prompt shows how to add another validation check inside the loop. Notice how you can reuse the same `continue` pattern you used for missing data.

**Filter high-value sales**

> "Write a function that takes the list of sales amounts and a minimum value, and returns only the sales at or above that value."

This prompt demonstrates a function with two parameters that returns a new list. You can then call it from the main program and display the results separately.

**Save the report to a file**

> "How can I write the sales report to a text file instead of only printing it?"

This prompt introduces writing to files. Notice how `with open(..., "w")` mirrors the reading code you wrote earlier.
