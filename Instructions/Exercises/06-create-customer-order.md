---
lab:
    title: 'Build a coffee shop order tracker'
    description: 'Write a Python program that uses a dictionary of menu items, a list to track a customer''s order, and loops to print a formatted receipt.'
    level: 100
    duration: 25
    islab: true
    status: 'released'
---

# Build a coffee shop order tracker

In this exercise, you build a small ordering app for a coffee shop. You practice using a **dictionary** to store menu items and prices, a **list** to track a customer's order, `for` and `while` loops to walk through data and collect input, and f-strings to format currency in a printed receipt.

This exercise takes approximately **25** minutes.

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

1. In the VS Code file explorer, navigate to the `Labfiles/06-create-customer-order` subfolder.

2. Select the `shop.py` file. This starter code already includes some prewritten code—welcome messages, an input loop that collects each order, and the receipt header. Your job is to fill in the empty sections marked with comments.

    ```python
    # Initialize the menu dictionary with items and prices


    # Track the customer's total order


    # Prompt the customer for their order
    print("Welcome to the Coffee Shop!")
    print("What would you like to order?")

    # Display the menu items and prices


    # Loop to take the customer's order
    while True:
        # Get the customer's choice
        choice = input("Enter an item (or type 'done' to finish): ").lower()

        # Check if the customer is done ordering
        if choice == 'done':
            break

        # Check if the choice is valid


    print("\nThank you for your order! Here is your receipt:")
    print("--- Receipt ---")

    # Loop through each item in the customer's order list


    print("---------------")

    # Display the final calculated total
    ```

3. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Initialize the menu dictionary

You'll represent the shop's menu as a **dictionary**. Each key is the name of a menu item, and each value is the price of that item.

1. Beneath the comment `# Initialize the menu dictionary with items and prices`, add the following lines:

    ```python
    menu = {
        "espresso": 3.00,
        "croissant": 3.50,
        "muffin": 2.75,
        "tea": 2.50
    }
    ```

    This code creates a dictionary called `menu` with four items and their prices.
    - Using the item name as the key lets you look up prices by name later.
    - Prices are stored as **floats** so calculations return decimal results.

## Track the customer's total order

To keep track of what a customer orders and how much it costs, you need two variables: a **list** to hold each item they add, and a running total that starts at zero.

1. Beneath the comment `# Track the customer's total order`, add the following lines:

    ```python
    total_bill = 0.0
    order = []
    ```

    - `total_bill = 0.0` starts as a float so the total keeps decimal precision as items are added.
    - `order = []` is an empty list that grows every time the customer adds an item.

## Display the menu items and prices

Before the customer types anything, they need to know what's on offer. You'll loop over the menu dictionary and print each item alongside its price.

1. Beneath the comment `# Display the menu items and prices`, add the following lines:

    ```python
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price:.2f}")
    ```

    - `menu.items()` gives you each `(item, price)` pair as you loop.
    - `.capitalize()` makes the item name look nicer in the output (`Espresso` instead of `espresso`).
    - `:.2f` formats the price with exactly two decimal places (e.g., `3.00` instead of `3.0`).

2. Select the **▶ Run Python File** button in the top-right corner of the editor, or open the terminal (**Terminal > New Terminal**) and run:

    ```bash
    python shop.py
    ```

    You should see the menu displayed. However, the program doesn't yet handle the customer's input, so it will wait for you to type something. Type `done` and press **Enter** to exit the program.

## Validate the customer's choice

Now you'll decide what to do with whatever the customer types. If the input matches an item on the menu, add it to their order. Otherwise, let them know it's not available.

1. Beneath the `# Check if the choice is valid` comment (inside the `while` loop), add the following lines:

    ```python
    if choice in menu:
        order.append(choice)
        print(f"Added {choice} to your order.")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")
    ```

    > **Note**: Keep the same indentation as the surrounding lines — this code belongs inside the `while` loop.

    - `in menu` checks whether `choice` is a key in the dictionary. It only returns `True` for items on the menu.
    - `.append(choice)` adds the item to the customer's `order` list.

2. Run the program. Order a few items, and try typing something invalid too. When you're finished, type `done`—the loop ends and you'll see the receipt header appear, followed by an empty section. You'll fill that in next.

## Build the receipt line by line

When the customer types `done`, the receipt starts printing. Now you need to walk through every item in the order, look up its price, print a receipt line, and add the price to the running total.

1. Add the following code under the comment `# Add each item in the order to the receipt and calculate the total`:

    ```python
    for item in order:
        price = menu[item]
        print(f"Item: {item.capitalize()} - ${price:.2f}")
        total_bill += price
    ```

    In this loop, each item in the `order` list is processed one at a time.
    - `menu[item]` looks up the price for the current ordered item.
    - The item and price are printed in a formatted line.
    - `total_bill += price` is shorthand for `total_bill = total_bill + price` — it adds each item's price to the running total.

## Display the final total

Now you'll print the total bill at the end of the receipt.

1. Beneath the `# Display the final calculated total` comment, add the following line:

    ```python
    print(f"Total Bill: ${total_bill:.2f}")
    ```

1. Your complete program should now look like this:

    ```python
    # Initialize the menu dictionary with items and prices
    menu = {
        "espresso": 3.00,
        "croissant": 3.50,
        "muffin": 2.75,
        "tea": 2.50
    }

    # Track the customer's total order
    total_bill = 0.0
    order = []

    # Prompt the customer for their order
    print("Welcome to the Coffee Shop!")
    print("What would you like to order?")

    # Display the menu items and prices
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price:.2f}")

    # Loop to take the customer's order
    while True:
        # Get the customer's choice
        choice = input("Enter an item (or type 'done' to finish): ").lower()

        # Check if the customer is done ordering
        if choice == 'done':
            break

        # Check if the choice is valid
        if choice in menu:
            order.append(choice)
            print(f"Added {choice} to your order.")
        else:
            print("Sorry, we don't have that item. Please choose from the menu.")


    print("\nThank you for your order! Here is your receipt:")
    print("--- Receipt ---")

    # Add each item in the order to the receipt and calculate the total
    for item in order:
        price = menu[item]
        print(f"Item: {item.capitalize()} - ${price:.2f}")
        total_bill += price

    print("---------------")

    # Display the final calculated total
    print(f"Total Bill: ${total_bill:.2f}")
    ```

1. Run the program one more time and place a full order to see the receipt in action. Try ordering an espresso, two croissants, and a muffin, then type `done`. You should see output similar to:

    ```output
    Welcome to the Coffee Shop!
    What would you like to order?
    Espresso: $3.00
    Croissant: $3.50
    Muffin: $2.75
    Tea: $2.50
    Enter an item (or type 'done' to finish): espresso
    Added espresso to your order.
    Enter an item (or type 'done' to finish): croissant
    Added croissant to your order.
    Enter an item (or type 'done' to finish): croissant
    Added croissant to your order.
    Enter an item (or type 'done' to finish): muffin
    Added muffin to your order.
    Enter an item (or type 'done' to finish): done

    Thank you for your order! Here is your receipt:
    --- Receipt ---
    Item: Espresso - $3.00
    Item: Croissant - $3.50
    Item: Croissant - $3.50
    Item: Muffin - $2.75
    ---------------
    Total Bill: $12.75
    ```

## Extend with GitHub Copilot

Now that the order tracker is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Group duplicate items on the receipt**

> "How can I group duplicate items in a list and count how many times each item appears?"

If a customer orders three espressos, the receipt currently shows three separate lines. Ask the AI about `collections.Counter`, then update your receipt loop so each item appears once with a quantity next to it.

**Add tax to the total**

> "Modify this code to add a 10% tax to the total bill and print the tax amount on the receipt."

Real receipts include tax. Ask the AI to show you a beginner-friendly example of adding a 10% tax, then print a tax line above the total and roll it into the final bill.

**Undo the customer's last item**

> "A customer changes their mind. How can I remove the last item they added to their order list?"

Sometimes a customer changes their mind. Ask the AI about the list `.pop()` method, then add an `"undo"` option to the order loop that removes the most recently added item and prints a confirmation.
