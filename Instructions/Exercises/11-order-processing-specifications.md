---
lab:
    title: 'Write specifications for GitHub Copilot'
    description: 'Deconstruct a feature request, write an explicit specification, and define edge cases. Then use GitHub Copilot to generate the code and verify that it follows your specification.'
    level: 200
    duration: 30
    islab: true
    status: 'released'
---

# Write specifications for GitHub Copilot

In this exercise, you turn a vague feature request into a specification, and then use GitHub Copilot to write the code from it. You deconstruct the request, write an explicit specification, and define edge cases. You don't write any Python yourself. Instead, you practice describing what you need clearly enough for AI to build it correctly.

This exercise takes approximately **30** minutes.

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

1. In the VS Code file explorer, navigate to the `Labfiles/11-order-processing-specifications` subfolder.

1. Select the `shipping.py` file.

    The file contains the feature request and a comment for each part of the specification you write:

    ```python
    # Feature request: Add shipping costs to customer orders.

    # Deconstruct the request

    # Write the explicit specification

    # Define the edge cases
    ```

    A specification written as comments is ignored by Python. In the steps that follow, you add each part of the specification beneath its comment. GitHub Copilot writes the Python code.

1. Select the `check_spec.py` file.

    This file calls the `calculate_shipping()` function with example orders and reports `PASS` or `FAIL` for each one. The examples include typical orders and unusual ones, so you can see how the code handles both. You don't edit this file.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

1. Make sure you're signed in to GitHub Copilot. You should see the Copilot icon in the bottom status bar.

1. Open a terminal (**Terminal > New Terminal**) and change to the exercise folder:

    ```bash
    cd Labfiles/11-order-processing-specifications
    ```

## Understand the shipping scenario

Before you begin writing your spec, take a moment to understand the shipping scenario and the requirements for calculating shipping costs.

You're building part of the checkout for an online store. When a customer places an order, the store needs to add a shipping cost. The store owner gave you this request:

> "Add shipping costs to customer orders."

The request doesn't say how much shipping costs or how to calculate it. When you ask, the owner describes the store's shipping policy:

- Orders over $50 ship for free.
- All other orders are charged by weight:
  - Light packages (under 1 kg) cost $5.
  - Medium packages (1 kg through 5 kg) cost $10.
  - Heavy packages (over 5 kg) cost $20.

The owner doesn't say what should happen for unusual orders, such as an order with no weight. You decide that when you define the edge cases.

The goal is a Python function named `calculate_shipping()`. It takes the weight of an order and the order total, and returns the shipping cost. The checkout code can then call it for any order.

You don't write the function yourself. You write a specification that's clear enough for GitHub Copilot to write it correctly, and then you use `check_spec.py` to verify the result. You work in three stages:

- **Deconstruct** the request into inputs, outputs, and rules.
- **Write** an explicit specification.
- **Define** the edge cases.

## Deconstruct the feature request

The request "Add shipping costs to customer orders" is too vague to build from. To deconstruct it, you ask what the system does, what goes in, what comes out, and what can go wrong. Use the store's shipping policy to answer each question.

1. Beneath the `# Deconstruct the request` comment, add the following lines:

    ```python
    # What does the system do?
    #   Calculates the shipping cost for one order.
    # What goes in?
    #   The weight of the order in kilograms and the order total in dollars.
    # What comes out?
    #   The shipping cost in dollars.
    # What can go wrong?
    #   The weight or the order total might be missing or invalid.
    ```

    - Each question has a one-line answer.
    - The vague request is now one small piece of work: a calculation with two inputs and one output.
    - The last answer is general. You define exactly what happens in the edge cases section.

## Write the explicit specification

Next, turn those answers and the shipping policy into a specification that leaves no room for guessing. An explicit specification states the inputs, the processing rules, the output, and examples.

1. Beneath the `# Write the explicit specification` comment, add the following lines:

    ```python
    # Function: calculate_shipping
    # Inputs:
    #   - weight_kg: a number (the weight of the order in kilograms)
    #   - order_total: a number (the order total in dollars)
    # Processing:
    #   1. If the order total is over 50.00, shipping is free.
    #   2. Otherwise, the shipping cost depends on the weight:
    #      - Under 1 kg: 5.00
    #      - From 1 kg through 5 kg: 10.00
    #      - Over 5 kg: 20.00
    # Output: the shipping cost in dollars, as a number
    ```

    - The function name and the input names tell Copilot exactly what to create.
    - Each input has a type and a unit.
    - The processing rules are numbered in the order they apply, so free shipping is checked first.
    - Each weight tier states its range and its cost.

1. Beneath the `# Output: the shipping cost in dollars, as a number` comment, add the following lines:

    ```python
    # Examples:
    #   calculate_shipping(0.5, 20.00)  -> 5.00
    #   calculate_shipping(3, 20.00)    -> 10.00
    #   calculate_shipping(8, 20.00)    -> 20.00
    #   calculate_shipping(3, 60.00)    -> 0.00
    ```

    Examples show the expected result for typical orders. You use them later to check the code that Copilot writes.

## Generate the code with GitHub Copilot

1. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**).

1. With `shipping.py` open in the editor, enter the following prompt:

    > "Write the Python function described in the specification comments in shipping.py. Follow the specification exactly, and don't add behavior that the specification doesn't describe."

    Copilot reads the comments in the file as the requirements. The last part of the prompt stops it from adding behavior that you didn't specify.

1. Review Copilot's response. Your code might differ, but it should look similar to the following:

    ```python
    def calculate_shipping(weight_kg, order_total):
        if order_total > 50:
            return 0.0
        if weight_kg < 1:
            return 5.0
        if weight_kg <= 5:
            return 10.0
        return 20.0
    ```

1. Compare the code with your specification. Check that free shipping is tested first, and that the weight tiers match the ranges in your specification.

1. Add the function to the end of `shipping.py`. Select **Apply in Editor** on the code block, or copy the code and paste it beneath the specification.

1. Run the checks in the terminal:

    ```bash
    python check_spec.py
    ```

1. Verify the output:

    ```output
    PASS  calculate_shipping(0.5, 20.0)        -> 5.0        expected 5.0
    PASS  calculate_shipping(3, 20.0)          -> 10.0       expected 10.0
    PASS  calculate_shipping(8, 20.0)          -> 20.0       expected 20.0
    PASS  calculate_shipping(3, 60.0)          -> 0.0        expected 0.0
    PASS  calculate_shipping(1, 20.0)          -> 10.0       expected 10.0
    PASS  calculate_shipping(5, 20.0)          -> 10.0       expected 10.0
    PASS  calculate_shipping(3, 50.0)          -> 10.0       expected 10.0
    FAIL  calculate_shipping(0, 20.0)          -> 5.0        expected error
    FAIL  calculate_shipping(-2, 20.0)         -> 5.0        expected error
    FAIL  calculate_shipping(3, -10.0)         -> 10.0       expected error
    FAIL  calculate_shipping('heavy', 20.0)    -> TypeError  expected error
    ```

    The orders with valid input pass. The last four rows fail because the function accepts a weight of 0 or less, accepts a negative order total, and crashes when it receives text. Your specification doesn't say what to do with this input, so Copilot didn't handle it. Your results might differ, depending on the code that Copilot wrote.

    Use the failing rows as your starting point for the next section.

## Define the edge cases

**Edge cases** are inputs at the boundaries of what a function accepts. For each one, the specification states the condition and exactly what the function does. The failing rows from the last check show three of them.

1. Beneath the `# Define the edge cases` comment, add the following lines:

    ```python
    # Edge cases:
    #   - If weight_kg is 0 or less, raise a ValueError with the message "weight_kg must be greater than 0".
    #   - If order_total is negative, raise a ValueError with the message "order_total can't be negative".
    #   - If weight_kg or order_total isn't a number, raise a ValueError with the message "weight_kg and order_total must be numbers".
    ```

    - Each edge case states the condition and the exact result.
    - In Python, a function reports an error by raising an exception such as `ValueError`. The message tells the caller what went wrong.

1. Beneath the last edge case that you added, add the following lines:

    ```python
    #   - An order_total of exactly 50.00 isn't over 50.00, so shipping is charged by weight.
    #   - A weight_kg of exactly 1 or exactly 5 is in the 1 kg through 5 kg tier.
    ```

    Boundaries are the values where two rules meet. Stating them removes any guesswork.

1. Scroll up to the examples in your specification. Beneath the `#   calculate_shipping(3, 60.00)    -> 0.00` comment, add the following lines:

    ```python
    #   calculate_shipping(1, 20.00)    -> 10.00
    #   calculate_shipping(5, 20.00)    -> 10.00
    #   calculate_shipping(3, 50.00)    -> 10.00
    #   calculate_shipping(0, 20.00)    -> error: weight_kg must be greater than 0
    #   calculate_shipping(3, -10.00)   -> error: order_total can't be negative
    #   calculate_shipping("heavy", 20) -> error: weight_kg and order_total must be numbers
    ```

    Add edge cases to your examples as well. They become part of the checklist for the code, and they match the rows that `check_spec.py` runs.

## Update the code with GitHub Copilot

1. In the Copilot Chat panel, enter the following prompt:

    > "The specification in shipping.py now includes edge cases and more examples. Update calculate_shipping so that it follows the complete specification."

1. Review Copilot's response. Your code might differ, but it should look similar to the following:

    ```python
    def calculate_shipping(weight_kg, order_total):
        if not isinstance(weight_kg, (int, float)) or not isinstance(order_total, (int, float)):
            raise ValueError("weight_kg and order_total must be numbers")
        if weight_kg <= 0:
            raise ValueError("weight_kg must be greater than 0")
        if order_total < 0:
            raise ValueError("order_total can't be negative")
        if order_total > 50:
            return 0.0
        if weight_kg < 1:
            return 5.0
        if weight_kg <= 5:
            return 10.0
        return 20.0
    ```

1. Update the function in `shipping.py`. Select **Apply in Editor** on the code block, or copy the code and paste it over the existing function. Make sure the file contains only one `calculate_shipping` function.

1. Run the checks again:

    ```bash
    python check_spec.py
    ```

1. Verify the output:

    ```output
    PASS  calculate_shipping(0.5, 20.0)        -> 5.0        expected 5.0
    PASS  calculate_shipping(3, 20.0)          -> 10.0       expected 10.0
    PASS  calculate_shipping(8, 20.0)          -> 20.0       expected 20.0
    PASS  calculate_shipping(3, 60.0)          -> 0.0        expected 0.0
    PASS  calculate_shipping(1, 20.0)          -> 10.0       expected 10.0
    PASS  calculate_shipping(5, 20.0)          -> 10.0       expected 10.0
    PASS  calculate_shipping(3, 50.0)          -> 10.0       expected 10.0
    PASS  calculate_shipping(0, 20.0)          -> error      expected error
    PASS  calculate_shipping(-2, 20.0)         -> error      expected error
    PASS  calculate_shipping(3, -10.0)         -> error      expected error
    PASS  calculate_shipping('heavy', 20.0)    -> error      expected error
    ```

    Every row passes. The code now handles the invalid input because your specification described it. The edge cases you wrote are what changed the result.

1. Your complete `shipping.py` should look similar to the following. The code at the end might differ:

    ```python
    # Feature request: Add shipping costs to customer orders.

    # Deconstruct the request
    # What does the system do?
    #   Calculates the shipping cost for one order.
    # What goes in?
    #   The weight of the order in kilograms and the order total in dollars.
    # What comes out?
    #   The shipping cost in dollars.
    # What can go wrong?
    #   The weight or the order total might be missing or invalid.

    # Write the explicit specification
    # Function: calculate_shipping
    # Inputs:
    #   - weight_kg: a number (the weight of the order in kilograms)
    #   - order_total: a number (the order total in dollars)
    # Processing:
    #   1. If the order total is over 50.00, shipping is free.
    #   2. Otherwise, the shipping cost depends on the weight:
    #      - Under 1 kg: 5.00
    #      - From 1 kg through 5 kg: 10.00
    #      - Over 5 kg: 20.00
    # Output: the shipping cost in dollars, as a number
    # Examples:
    #   calculate_shipping(0.5, 20.00)  -> 5.00
    #   calculate_shipping(3, 20.00)    -> 10.00
    #   calculate_shipping(8, 20.00)    -> 20.00
    #   calculate_shipping(3, 60.00)    -> 0.00
    #   calculate_shipping(1, 20.00)    -> 10.00
    #   calculate_shipping(5, 20.00)    -> 10.00
    #   calculate_shipping(3, 50.00)    -> 10.00
    #   calculate_shipping(0, 20.00)    -> error: weight_kg must be greater than 0
    #   calculate_shipping(3, -10.00)   -> error: order_total can't be negative
    #   calculate_shipping("heavy", 20) -> error: weight_kg and order_total must be numbers

    # Define the edge cases
    # Edge cases:
    #   - If weight_kg is 0 or less, raise a ValueError with the message "weight_kg must be greater than 0".
    #   - If order_total is negative, raise a ValueError with the message "order_total can't be negative".
    #   - If weight_kg or order_total isn't a number, raise a ValueError with the message "weight_kg and order_total must be numbers".
    #   - An order_total of exactly 50.00 isn't over 50.00, so shipping is charged by weight.
    #   - A weight_kg of exactly 1 or exactly 5 is in the 1 kg through 5 kg tier.

    def calculate_shipping(weight_kg, order_total):
        if not isinstance(weight_kg, (int, float)) or not isinstance(order_total, (int, float)):
            raise ValueError("weight_kg and order_total must be numbers")
        if weight_kg <= 0:
            raise ValueError("weight_kg must be greater than 0")
        if order_total < 0:
            raise ValueError("order_total can't be negative")
        if order_total > 50:
            return 0.0
        if weight_kg < 1:
            return 5.0
        if weight_kg <= 5:
            return 10.0
        return 20.0
    ```

## Extend with GitHub Copilot

Now that your specification produces working code, use GitHub Copilot to improve it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Find gaps in your specification**

> "Review the specification comments in shipping.py. What is unclear, missing, or open to interpretation? Don't change the file."

Compare the answer with your own edge cases. Decide which gaps are worth adding to the specification.

**Generate tests from your examples**

> "Write unit tests in test_shipping.py using unittest. Create one test for each example in the specification in shipping.py."

Run the tests with `python -m unittest test_shipping -v`. The examples in a specification become a test checklist for the code.
