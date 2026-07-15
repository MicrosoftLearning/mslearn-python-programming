---
lab:
    title: 'Create an inventory manager'
    description: 'Write a Python program that uses lists and a dictionary to track products, quantities, and updates in a simple inventory manager.'
    level: 100
    duration: 25
    islab: true
    status: 'released'
---

# Create an inventory manager

In this exercise, you build a small inventory manager for a shop. You practice using a **dictionary** to store products and their quantities, a **list** to define the menu options, and a `while` loop with `if`/`elif`/`else` to react to what the user chooses.

This exercise takes approximately **25** minutes.

## Set up your workspace

You'll write and run your code in Visual Studio Code.

1. Open **Visual Studio Code**.

1. Select **File > Open Folder**, create a new folder called `inventory-manager` somewhere on your machine, and open it.

1. In the **Explorer** panel, select the **New File** icon and name the file `inventory.py`.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Set up your starter code

Before writing any logic, you'll paste a set of guiding comments into `inventory.py`. These comments act as an outline for your program — each one marks where a specific piece of code belongs.

1. Copy the following comments and paste them into `inventory.py`:

    ```python
    # Set up the starting inventory

    # Show the menu

    # Run the main program loop

    # Handle the user's choice
    ```

    Remember, comments are ignored by Python when the program runs. They're just there to help you organize your code.

1. Leave the code as-is for now. In the steps that follow, you'll add code beneath each comment.

## Set up the starting inventory

You'll represent the inventory as a **dictionary** where each key is a product name and each value is the quantity in stock. You'll also define the menu options as a **list**.

1. Beneath the `# Set up the starting inventory` comment, add the following lines:

    ```python
    inventory = {
        "apples":  12,
        "bread":    5,
        "eggs":    24,
        "milk":     3
    }

    menu_options = ["view", "add", "remove", "quit"]
    ```

    - `inventory` uses each product name as a key. Later, you'll look up quantities by name.
    - `menu_options` is a list you can print to remind the user of their choices, and use to validate their input.

1. Select the **▶ Run Python File** button in the top-right corner of the editor, or open the terminal (**Terminal > New Terminal**) and run:

    ```bash
    python inventory.py
    ```

    The program should run without errors. You won't see output yet — you'll add that next.

## Show the menu

Now you'll write the code that displays the current inventory and the list of menu options. You'll use a `for` loop to walk through the dictionary's key-value pairs, and another one to print the menu options.

1. Beneath the `# Show the menu` comment, add the following lines:

    ```python
    print("\n--- Current inventory ---")
    for product, quantity in inventory.items():
        print(f"  {product}: {quantity}")

    print("\nWhat would you like to do?")
    for option in menu_options:
        print(f"  - {option}")
    ```

    - `inventory.items()` gives you each `product` and `quantity` pair as you loop through the dictionary.
    - The second `for` loop prints each menu option on its own line.

1. Run the program. You should see:

    ```output
    --- Current inventory ---
      apples: 12
      bread: 5
      eggs: 24
      milk: 3

    What would you like to do?
      - view
      - add
      - remove
      - quit
    ```

## Run the main program loop

A real inventory app shouldn't quit after one action. You'll use a `while` loop so the user can keep making choices until they decide to quit. To do that, you'll wrap the menu code you just wrote inside the loop.

1. Beneath the `# Run the main program loop` comment, add the following lines:

    ```python
    while True:
        choice = input("\nEnter a choice: ").lower()

        if choice not in menu_options:
            print("That's not a valid option. Try again.")
            continue

        if choice == "quit":
            print("Goodbye!")
            break
    ```

    - `while True:` runs forever until `break` stops it — the `quit` option is what triggers that.
    - `.lower()` converts the input to lowercase so `"Add"` and `"add"` are treated the same.
    - `continue` skips the rest of this loop iteration if the user typed something that isn't in `menu_options`.

1. Move the menu-display code (the two `for` loops beneath `# Show the menu`) so it sits **inside** the `while` loop, right at the top. That way, the menu shows up again every time through the loop. Your loop should look like this:

    ```python
    while True:
        print("\n--- Current inventory ---")
        for product, quantity in inventory.items():
            print(f"  {product}: {quantity}")

        print("\nWhat would you like to do?")
        for option in menu_options:
            print(f"  - {option}")

        choice = input("\nEnter a choice: ").lower()

        if choice not in menu_options:
            print("That's not a valid option. Try again.")
            continue

        if choice == "quit":
            print("Goodbye!")
            break
    ```

1. Run the program. Try entering `quit` at the prompt — the program should say goodbye and stop. Try entering something like `xyz` — it should tell you the option is invalid and reprint the menu.

## Handle the view, add, and remove options

Now you'll add the code that actually reacts to `view`, `add`, and `remove`. Each one uses a different way of working with the dictionary.

1. Beneath the `if choice == "quit":` block (still inside the `while` loop), add the following:

    ```python
        if choice == "view":
            product = input("Which product do you want to check? ").lower()
            quantity = inventory.get(product, 0)
            print(f"There are {quantity} {product} in stock.")

        elif choice == "add":
            product = input("Which product do you want to add? ").lower()
            amount = int(input("How many? "))
            inventory[product] = inventory.get(product, 0) + amount
            print(f"Added {amount} {product}. New total: {inventory[product]}.")

        elif choice == "remove":
            product = input("Which product do you want to remove? ").lower()
            amount = int(input("How many? "))
            current = inventory.get(product, 0)
            if amount > current:
                print(f"You only have {current} {product} in stock.")
            else:
                inventory[product] = current - amount
                print(f"Removed {amount} {product}. New total: {inventory[product]}.")
    ```

    - `inventory.get(product, 0)` returns the quantity for `product`, or `0` if the product isn't in the dictionary. This prevents a `KeyError` when a user checks for something new.
    - The `add` block **adds a new key** if the product doesn't exist yet, or **updates the existing value** if it does.
    - The `remove` block guards against removing more than what's in stock.

1. Your complete program should now look like this:

    ```python
    # Set up the starting inventory
    inventory = {
        "apples":  12,
        "bread":    5,
        "eggs":    24,
        "milk":     3
    }

    menu_options = ["view", "add", "remove", "quit"]

    # Run the main program loop
    while True:
        # Show the menu
        print("\n--- Current inventory ---")
        for product, quantity in inventory.items():
            print(f"  {product}: {quantity}")

        print("\nWhat would you like to do?")
        for option in menu_options:
            print(f"  - {option}")

        choice = input("\nEnter a choice: ").lower()

        # Handle the user's choice
        if choice not in menu_options:
            print("That's not a valid option. Try again.")
            continue

        if choice == "quit":
            print("Goodbye!")
            break

        if choice == "view":
            product = input("Which product do you want to check? ").lower()
            quantity = inventory.get(product, 0)
            print(f"There are {quantity} {product} in stock.")

        elif choice == "add":
            product = input("Which product do you want to add? ").lower()
            amount = int(input("How many? "))
            inventory[product] = inventory.get(product, 0) + amount
            print(f"Added {amount} {product}. New total: {inventory[product]}.")

        elif choice == "remove":
            product = input("Which product do you want to remove? ").lower()
            amount = int(input("How many? "))
            current = inventory.get(product, 0)
            if amount > current:
                print(f"You only have {current} {product} in stock.")
            else:
                inventory[product] = current - amount
                print(f"Removed {amount} {product}. New total: {inventory[product]}.")
    ```

1. Run the program and try each option. Add some `oranges`, remove some `eggs`, view how many `milk` you have left, and then quit.

## Extend with GitHub Copilot

Now that the inventory manager is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Find the most-stocked product**

> "In Python, how do I find the key with the largest value in a dictionary?"

Your inventory would be more useful if it could highlight which product has the highest quantity. Ask the AI how `max()` works with a `key` argument, then add a line to your menu display that shows the top-stocked product.

**Delete a product entirely**

> "In Python, how do I safely delete a key from a dictionary without crashing if the key isn't there?"

Right now, `remove` only reduces the quantity. Ask the AI about the `.pop()` method, then add a new `"delete"` menu option that removes a product from the dictionary completely. Don't forget to add `"delete"` to `menu_options`.

**Sort the inventory display**

> "In Python, how can I sort a dictionary alphabetically by key when I display it?"

The inventory currently prints in the order items were added. Ask the AI how to use `sorted()`, then update your display loop so products always appear in alphabetical order.
