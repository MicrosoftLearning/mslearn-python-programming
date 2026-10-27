---
lab:
    title: 'Refactor a sales report generator to code defensively'
    description: 'Improve a Python sales report program so that it is readable, documented, handles bad data, and is covered by unit tests.'
    level: 200
    duration: 40
    islab: true
    status: 'released'
---

# Refactor a sales report generator to code defensively

A teammate wrote a program that reads sales data from a CSV file and prints a report. It works on clean data, but it crashes on real data. In this exercise, you refactor the program so that it's readable, handles bad data, is documented, and has unit tests. Then you use GitHub Copilot to find and fix a gap you missed.

This exercise takes approximately **40** minutes.

## Set up your workspace

You write and run your code in Visual Studio Code. The starter code is in a GitHub repository.

> **Tip**: If you already cloned the repository in another exercise, skip to the next section.

1. Open a new **Visual Studio Code** window (**File > New Window**).

1. On the Welcome page, select **Clone Git Repository...**, or open the Command Palette (**Ctrl+Shift+P**) and run **Git: Clone**.

1. Enter the following URL and press **Enter**:

    ```
    https://github.com/MicrosoftLearning/mslearn-python-programming.git
    ```

1. Create a folder for the repository, such as `mslearn-python`, and select **Select as Repository Destination**.

1. When the clone completes, select **Open**.

## Review and run the starter code

1. In the Explorer pane, open the `Labfiles/09-sales-report-generator` folder. It contains three files:

    | File | Purpose |
    |---|---|
    | `sales_report.py` | The program you refactor. |
    | `sales.csv` | The sales data. |
    | `test_sales_report.py` | Unit tests that you extend. |

1. Open `sales.csv`. Some rows are intentionally bad:

    ```text
    Date,Product,Amount
    2024-01-15,Widget A,1500.00
    2024-01-15,Widget B,2100.00
    2024-01-15,Widget C,INVALID
    2024-01-16,Widget A,1200.00
    2024-01-16,Widget B
    2024-01-17,Widget C,450.00
    2024-01-17,Widget A,-50.00
    ```

    Line 4 has a non-numeric amount, line 6 has no amount, and line 8 has a negative amount.

1. Open `sales_report.py` and review the code:

    | Function | Purpose |
    |---|---|
    | `parse_sales_row` | Reads the amount from one row. It already validates the row and raises `ValueError` for bad data. |
    | `rd` | Reads the file and returns a list of amounts. |
    | `avg` | Calculates the average of the amounts. |
    | `display_sales_report` | Prints the report. |

    The `if __name__ == "__main__":` block at the bottom runs the program. It runs only when you run the file directly, so your tests can import the functions without printing a report.

1. Open a terminal (**Terminal > New Terminal**), change to the exercise folder, and run the program:

    ```bash
    cd Labfiles/09-sales-report-generator
    python sales_report.py
    ```

    The program crashes. The last line of the error is:

    ```output
    ValueError: could not convert string to float: 'INVALID'
    ```

    `parse_sales_row` correctly rejected the bad row, but nothing handles the exception, so the program stops. In the next sections, you fix this and the other weaknesses in the code.

## Make the code readable

The names `rd` and `avg` don't describe what the functions do. You rename them with VS Code, which updates every place the names are used.

1. Beneath the `# Read sales data from CSV file` comment, right-click `rd` in the `def` line and select **Rename Symbol**, or select `rd` and press **F2**. Enter `read_sales_data` and press **Enter**.

1. Beneath the `# Calculate statistics` comment, rename `avg` to `calculate_average` the same way.

1. Check that the calls in `display_sales_report` and in the `# Main program flow` block changed too. Run the program again. You get the same `ValueError` as before.

    Renaming changes how the code reads, not how it behaves.

## Handle errors

The program has three weaknesses: one bad row stops the whole report, a missing file crashes the program, and an empty list of sales causes a confusing error. In this section, you address each of these issues.

### Skip bad rows

A single bad row shouldn't stop the whole report. `parse_sales_row` already raises a `ValueError` for a bad row. You catch that exception in the loop so the program reports the problem and moves on to the next row.

> **Tip**: As you add code, be sure to maintain the correct indentation. Use the existing comments as a guide, entering the new code at the same level of indentation.

1. Beneath the `# Skip a row that parse_sales_row rejects and print its line number` comment, update the code to the following:

    ```python
    try:
        sales_amounts.append(parse_sales_row(line))
    except ValueError as error:
        print(f"Line {line_number}: {error} - skipped")
    ```

    - The `append` line moves inside the `try` block, so a row is added to the list only if `parse_sales_row` accepts it.
    - `except ValueError as error` runs when `parse_sales_row` raises an exception. The variable `error` holds the message.
    - The loop already numbers each row with `enumerate(file, start=2)`. The count starts at `2` because the header is line 1. You use `line_number` to tell the user which row was skipped.

2. Run the program. The report prints, and each bad row is reported:

    ```output
    Reading sales from sales.csv...
    Line 4: could not convert string to float: 'INVALID' - skipped
    Line 6: row is missing the amount - skipped
    Line 8: amount must be greater than zero - skipped
    Sales Report
    ========================================
    Total Sales:        $5,250.00
    Average Sale:       $1,312.50
    Highest Sale:       $2,100.00
    Lowest Sale:        $450.00
    Number of Sales:    4
    ========================================
    ```

### Handle a missing file

`read_sales_data` shouldn't decide what happens when the file is missing. The code that calls it should. When the file doesn't exist, `open()` raises a `FileNotFoundError`, and the exception passes up to the caller. You catch it in the main program flow.

1. Beneath the `# If the file isn't found, print an error message and use an empty list` comment, update the code to the following:

    ```python
    try:
        sales_amounts = read_sales_data(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sales_amounts = []
    ```

    - The call to `read_sales_data` moves inside the `try` block.
    - `except FileNotFoundError` prints a clear message instead of a traceback.
    - `sales_amounts = []` gives `display_sales_report` an empty list, so it prints its "No valid sales data found." message and the program ends normally.

1. To test it, beneath the `# Main program flow` comment, update the `filename` line to the following:

    ```python
    filename = "missing.csv"
    ```

1. Run the program:

    ```output
    Reading sales from missing.csv...
    Error: File 'missing.csv' not found
    Sales Report
    ========================================
    No valid sales data found.
    ```

1. Beneath the `# Main program flow` comment, update the `filename` line back to the following:

    ```python
    filename = "sales.csv"
    ```

### Reject an empty list

`display_sales_report` checks for an empty list before it calls `calculate_average`. But other code might call `calculate_average` directly. With an empty list, the function fails with `ZeroDivisionError`, which doesn't explain the real problem. You add a check that raises a clearer exception.

1. Beneath the `# Raise a ValueError if the list of sales amounts is empty` comment, add the following lines:

    ```python
    if len(sales_amounts) == 0:
        raise ValueError("Can't calculate the average of an empty list")
    ```

    - The `if` statement checks the input before the calculation runs.
    - `raise ValueError(...)` stops the function with a message that explains what went wrong. The caller decides how to respond.

1. Run the program. The output doesn't change, because `display_sales_report` never passes an empty list. You confirm the new check with a unit test later in this exercise.

## Document the function

You changed what `calculate_average` does for an empty list, but a reader can't tell that from the function's first line. You add type hints and a docstring so they know what to pass in, what comes back, and what can go wrong.

1. Beneath the `# Add type hints and a docstring that describes the ValueError` comment, update the function definition to the following:

    ```python
    def calculate_average(sales_amounts: list[float]) -> float:
        """Return the average of the sales amounts.

        Raises ValueError if the list is empty.
        """
    ```

    - `list[float]` shows that the function expects a list of numbers, and `-> float` shows that it returns a number.
    - The docstring describes the result and the exception that you added.
    - The `if` statement and the `return` line beneath the docstring stay the same.

1. Beneath the `# Display report` comment, hover over `calculate_average` in the `display_sales_report` function. VS Code shows the docstring and the type hints.

    `parse_sales_row` already has both, so you can use it as a model.

## Add unit tests

Tests confirm that your error handling keeps working when the code changes. You write one test for each place where the program rejects bad input.

1. Open `test_sales_report.py`. It has two tests for normal input and two comments that describe the tests you add.

1. Beneath the `# Test that calculate_average raises ValueError for an empty list` comment, add the following test:

    ```python
    def test_calculate_average_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])
    ```

    - `assertRaises` passes only when the code inside the `with` block raises the exception. If `calculate_average([])` returns a value or raises a different exception, the test fails.
    - This test confirms the check that you added to `calculate_average`.

1. Beneath the `# Test that parse_sales_row raises ValueError for an amount that isn't a number` comment, add the following test:

    ```python
    def test_parse_sales_row_invalid_amount(self):
        with self.assertRaises(ValueError):
            parse_sales_row("2024-01-15,Widget C,INVALID")
    ```

    - The test passes a row with the text `INVALID` where the amount belongs.
    - This test confirms the validation in `parse_sales_row`.

    Keep both tests indented inside the `TestSalesReport` class, at the same level as the existing tests.

1. Run the tests from the terminal:

    ```bash
    python -m unittest test_sales_report -v
    ```

    ```output
    test_calculate_average (test_sales_report.TestSalesReport.test_calculate_average) ... ok
    test_calculate_average_empty_list (test_sales_report.TestSalesReport.test_calculate_average_empty_list) ... ok
    test_parse_sales_row (test_sales_report.TestSalesReport.test_parse_sales_row) ... ok
    test_parse_sales_row_invalid_amount (test_sales_report.TestSalesReport.test_parse_sales_row_invalid_amount) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK
    ```

    > **Note**: The test names in the output depend on your Python version. Versions earlier than 3.11 print `test_calculate_average (test_sales_report.TestSalesReport)`.

## Practice with GitHub Copilot

The program handles the problems you knew about. Use GitHub Copilot to look for the ones you didn't. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts. Copilot can make mistakes, so read each response, and run the program and the tests before you accept a change.

**Document the rest of the code**

> "Add a docstring and type hints to `read_sales_data` and `display_sales_report`. Describe what each function does, what it returns, and what it prints."

This prompt applies the same documentation you added to `calculate_average`. Check the result. Does the `read_sales_data` docstring mention the skipped rows and the `FileNotFoundError` that it can raise? Are the type hints correct?

**Find the gaps**

> "What inputs could make `read_sales_data` crash or report misleading results? Don't change the code."

This prompt asks Copilot to review the code without editing it. Review the list it gives you. To try one possible gap, create an empty file named `empty.csv` in the exercise folder. Then beneath the `# Main program flow` comment, update the `filename` line to the following:

```python
filename = "empty.csv"
```

Run the program. It crashes with `StopIteration`, because `next(file)` finds no header row. Update the `filename` line back to the following:

```python
filename = "sales.csv"
```

**Fix the gap and prove the fix**

> "Update `read_sales_data` so that an empty file prints a clear message and returns an empty list. Then add a unit test that checks the fix."

This prompt asks for both a code change and a test that proves it works. Review the change. Run the program with `empty.csv` and `sales.csv`, then run the tests again. Keep the change only if the program and all the tests pass.

You started with a program that crashed on real data. You now have one that reports bad rows, handles missing and empty files, explains itself, and has tests that catch regressions.
