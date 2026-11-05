---
lab:
    title: 'Audit AI-generated code with GitHub Copilot'
    description: 'Find hallucinated functions, validation gaps, and unsafe logic in AI-generated Python code. Then fix the code and verify it with a checker script.'
    level: 200
    duration: 30
    islab: true
    status: 'released'
---

# Audit AI-generated code with GitHub Copilot

In this exercise, you audit a Python inventory module that an AI assistant generated. The module looks reasonable, but it has three problems: it calls functions that don't exist, it changes data without validating it, and it returns silent defaults that hide errors. You find each problem, use GitHub Copilot to help fix it, and then run a checker script that reports `PASS` or `FAIL` for each case.

This exercise takes approximately **30** minutes.

## Set up your workspace

You write and run your code in Visual Studio Code. The starter code for this exercise lives in a GitHub repository. Clone it now if you haven't already.

> **Tip**: If you've already cloned the repo during another exercise, skip to the next section.

1. Open a new **Visual Studio Code** window (**File > New Window**).

1. On the Welcome page, select **Clone Git Repository...** (or open the Command Palette with **Ctrl+Shift+P** and run **Git: Clone**).

1. Paste the following URL and press **Enter**:

    ```
    https://github.com/MicrosoftLearning/mslearn-python-programming.git
    ```

1. When the file selection dialog appears, create a new folder in a convenient location to hold the repo (for example, `mslearn-python`), select it, and click **Select as Repository Destination**.

1. After the clone completes, select **Open** to open the folder in VS Code.

1. Open a terminal (**Terminal > New Terminal**) and change to the exercise folder:

    ```bash
    cd Labfiles/12-inventory-management-code-review
    ```

1. Make sure your Python environment is active. You should see a Python version in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

1. Make sure you're signed in to GitHub Copilot. You should see the Copilot icon in the bottom status bar.

## Review the starter code

1. Select the `inventory_ai_generated.py` file.

    The file has an `INVENTORY` dictionary and three functions: `get_stock_level()`, `update_stock()`, and `transfer_stock()`. Each function has a comment that marks the issue you fix in this exercise.

1. Select the `check_inventory.py` file.

    This file runs 16 checks against the three functions and reports `PASS` or `FAIL` for each one. You don't edit this file; it's your definition of correct behavior.

## Run the starter code

1. In the terminal, run the file:

    ```bash
    python inventory_ai_generated.py
    ```

    The output is an error similar to the following:

    ```output
    NameError: name 'fetch_inventory' is not defined
    ```

    The AI called a function that doesn't exist in this code. This is a hallucination. Python can't run the program until you fix it.

1. Run the checker:

    ```bash
    python check_inventory.py
    ```

    Most rows show `FAIL`. Keep the output open. You rerun the checker after each fix.

## Issue 1: Replace a hallucinated function

To fix this issue, you correct a function that calls code that doesn't exist and that doesn't validate its inputs.

`get_stock_level()` calls `fetch_inventory()`, which doesn't exist. The function also has a second problem: it doesn't check for unknown products or warehouses.

1. Select the `get_stock_level()` function. In GitHub Copilot Chat, enter this prompt:

    ```
    The function get_stock_level calls fetch_inventory, which doesn't exist in this file.
    Rewrite it to read the stock level from the INVENTORY dictionary.
    If product_id is not in INVENTORY, raise ValueError with a message that names the product.
    If warehouse_id is not in INVENTORY[product_id], raise ValueError with a message that names the warehouse.
    Don't return 0 or None for unknown products or warehouses.
    Keep the function name and parameters the same.
    ```

1. Review the suggested code. Confirm that it doesn't call `fetch_inventory` and that it raises `ValueError` for both unknown inputs. Accept the change.

1. Run `python check_inventory.py`. The first four rows should now show `PASS`.

## Issue 2: Validate before you change data

To fix this issue, you correct a function that calls code that doesn't exist and changes stock without checking the input first.

`update_stock()` calls `update_inventory_sync()`, which doesn't exist. It also changes stock without any checks, so a negative change can drive a stock level below zero.

1. Select the `update_stock()` function. In GitHub Copilot Chat, enter this prompt:

    ```
    Rewrite update_stock so it follows these rules, in this order:
    1. Raise ValueError("Unknown product: <product_id>") if product_id isn't in INVENTORY.
    2. Raise ValueError("Unknown warehouse: <warehouse_id>") if warehouse_id isn't in that product's entry.
    3. Raise ValueError("Quantity change must not be zero") if quantity_change is 0.
    4. Calculate the new level. If it's below 0, raise ValueError("Insufficient stock") and don't change INVENTORY.
    5. Otherwise, store the new level in INVENTORY and return it.
    Don't call any function that isn't defined in this file.
    ```

1. Review the code. Check that every check runs before INVENTORY is changed, and that the function doesn't call `update_inventory_sync`. Accept the change.

1. Run `python check_inventory.py`. The rows for `update_stock` should show `PASS`.

## Issue 3: Fix validation order in transfers

To fix this issue, you correct a function that changes stock before it finishes validating the transfer, which can leave the warehouses in an incorrect state.

`transfer_stock()` changes both warehouses before it checks anything. If the transfer fails halfway, the stock is wrong. It also doesn't reject a transfer to the same warehouse or a quantity of zero or less.

1. Select the `transfer_stock()` function. In GitHub Copilot Chat, enter this prompt:

    ```
    Rewrite transfer_stock so it follows these rules, in this order:
    1. Raise ValueError if product_id isn't in INVENTORY.
    2. Raise ValueError if from_warehouse or to_warehouse isn't in that product's entry.
    3. Raise ValueError("Quantity must be at least 1") if quantity is less than 1.
    4. Raise ValueError("Source and destination must differ") if from_warehouse equals to_warehouse.
    5. Raise ValueError("Insufficient stock") if from_warehouse has less than quantity.
    6. Only after all checks pass, subtract quantity from from_warehouse and add it to to_warehouse.
    Return a tuple: (new level in from_warehouse, new level in to_warehouse).
    ```

1. Review the code. Confirm that no INVENTORY value changes until all checks pass. Accept the change.

1. Run `python check_inventory.py`. All 16 rows should show `PASS`.

## Review with an audit checklist

Now review the complete file against this checklist. Use GitHub Copilot to help you look for each item. Don't change the code in this step.

1. In GitHub Copilot Chat, enter this prompt:

    ```
    Review inventory_ai_generated.py against this checklist. For each item, answer Yes or No and quote the line that supports your answer.
    1. Does every function call a function or method that is defined in this file or in Python's standard library?
    2. Do all validation checks run before any data changes?
    3. Does any function return a default value, such as 0, None, or an empty string, for invalid input instead of raising an error?
    4. Would the code still work correctly with 1,000,000 products instead of 3?
    5. Can a caller pass input that causes unsafe or unexpected behavior?
    Don't change the file. Only report the findings.
    ```

1. Read the answers. If Copilot reports a No that you haven't already fixed, decide whether it's a real problem. If it is, fix it by hand and rerun the checker. Item 4 is a discussion point, not a required fix for this exercise.

## Run the final checks

1. Run the checker one more time:

    ```bash
    python check_inventory.py
    ```

    The expected output has 16 rows, and every row shows `PASS`. The end of the output looks like this:

    ```output
    PASS  transfer_stock('INVALID', 'warehouse1', 'warehouse2', 5)       -> error        expected error
    ```

1. If any row shows `FAIL`, compare its `-> result` and `expected` values. Then reread the matching rule in the prompt for that issue. Rerun the checker after each fix.

## What you learned

In this exercise, you:

- Found a hallucinated function by running the code and reading the `NameError`.
- Replaced silent defaults with explicit errors, so invalid input can't pass unnoticed.
- Moved all validation before any data change, so a failed call leaves the data unchanged.
- Used an AI review checklist to look for problems you might have missed, and checked the results yourself.

The checker verified the behavior. Copilot helped with the code, but you decided what correct behavior means. Apply the same steps to any AI-generated code: run it, check the functions it calls, test the edge cases, and review it against a checklist before you rely on it.
