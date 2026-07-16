---
lab:
    title: 'Create a calculator'
    description: 'Write a Python program that uses functions with parameters and return values to build a simple interactive calculator.'
    level: 100
    duration: 25
    islab: true
    status: 'released'
---

# Create a calculator

In this exercise, you build a simple interactive calculator. You practice defining **functions** with parameters, returning values from them, and organizing your code around small, reusable pieces instead of one long script.

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

1. In the VS Code file explorer, navigate to the `Labfiles/08-create-a-calculator` subfolder.

1. Select the `calculator.py` file. You'll see a set of guiding comments that act as an outline for your program — each one marks where a specific piece of code belongs:

    ```python
    # Define the calculator functions

    # Show the menu

    # Run the main program loop

    # Perform the calculation
    ```

    Remember, comments are ignored by Python when the program runs. They're just there to help you organize your code. In the steps that follow, you'll add code beneath each comment.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Define functions for each operation

Instead of writing the arithmetic inline, you'll wrap each operation in its own function. Each function takes two parameters and **returns** a result — that way, the rest of the program doesn't have to know how the math is done.

1. Beneath the `# Define the calculator functions` comment, add the following:

    ```python
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return None
        return a / b
    ```

    - Each function takes two **parameters** (`a` and `b`) and gives back a value with `return`.
    - `divide` guards against division by zero by returning `None` — a special value that means "no result." The main loop will check for it and display a friendly message.

1. Select the **▶ Run Python File** button in the top-right corner of the editor, or open the terminal (**Terminal > New Terminal**) and run:

    ```bash
    python calculator.py
    ```

    The program should run without errors. You won't see output yet — defining functions doesn't call them, it just makes them available.

## Test your functions

You can quickly check that your functions work by calling them directly and printing the results.

1. Temporarily add the following lines at the bottom of your program to test the functions:

    ```python
    print(add(4, 5))          # Expect 9
    print(subtract(10, 3))    # Expect 7
    print(multiply(6, 7))     # Expect 42
    print(divide(20, 4))      # Expect 5.0
    print(divide(5, 0))       # Expect None
    ```

1. Run the program. You should see:

    ```output
    9
    7
    42
    5.0
    None
    ```

1. Once you're satisfied that the functions work, **delete** these test lines. You'll build the real interactive interface next.

## Show the menu

You'll offer the user four operations plus a way to quit. Keeping the menu options in a list makes it easy to display them and validate the user's choice.

1. Beneath the `# Show the menu` comment, add the following:

    ```python
    menu_options = ["add", "subtract", "multiply", "divide", "quit"]
    ```

## Run the main program loop

Now you'll wire everything together with a `while` loop that reads the user's choice, collects two numbers, and calls the right function.

1. Beneath the `# Run the main program loop` comment, add the following:

    ```python
    while True:
        print("\nWhat would you like to do?")
        for option in menu_options:
            print(f"  - {option}")

        choice = input("\nEnter an operation: ").lower()

        if choice not in menu_options:
            print("That's not a valid option. Try again.")
            continue

        if choice == "quit":
            print("Goodbye!")
            break

        # Collect two numbers
        a = float(input("First number:  "))
        b = float(input("Second number: "))
    ```

    - `float(input(...))` reads the user's input and converts it to a decimal number, so operations like `divide` return meaningful results.
    - The loop prints the menu again after every operation, so the user always knows what's available.

## Perform the calculation

The last piece is picking the right function based on the user's choice, calling it, and displaying the result. This is where the value returned from each function actually gets used.

1. Beneath the `# Perform the calculation` comment, add:

    ```python
        if choice == "add":
            result = add(a, b)
        elif choice == "subtract":
            result = subtract(a, b)
        elif choice == "multiply":
            result = multiply(a, b)
        elif choice == "divide":
            result = divide(a, b)

        if result is None:
            print("Can't divide by zero.")
        else:
            print(f"Result: {result}")
    ```

    Be sure to indent this block so it's inside the `while` loop.

    - Each `elif` calls a different function and stores its return value in `result`.
    - `if result is None:` handles the divide-by-zero case cleanly — a nice benefit of returning `None` instead of crashing.

2. Your complete program should now look like this:

    ```python
    # Define the calculator functions
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return None
        return a / b

    # Show the menu
    menu_options = ["add", "subtract", "multiply", "divide", "quit"]

    # Run the main program loop
    while True:
        print("\nWhat would you like to do?")
        for option in menu_options:
            print(f"  - {option}")

        choice = input("\nEnter an operation: ").lower()

        if choice not in menu_options:
            print("That's not a valid option. Try again.")
            continue

        if choice == "quit":
            print("Goodbye!")
            break

        a = float(input("First number:  "))
        b = float(input("Second number: "))

        # Perform the calculation
        if choice == "add":
            result = add(a, b)
        elif choice == "subtract":
            result = subtract(a, b)
        elif choice == "multiply":
            result = multiply(a, b)
        elif choice == "divide":
            result = divide(a, b)

        if result is None:
            print("Can't divide by zero.")
        else:
            print(f"Result: {result}")
    ```

3. Run the program. Try each operation:

    ```output
    What would you like to do?
      - add
      - subtract
      - multiply
      - divide
      - quit

    Enter an operation: multiply
    First number:  6
    Second number: 7
    Result: 42.0
    ```

    Then try `divide` with `0` as the second number to make sure the "can't divide by zero" message shows up.

## Extend with GitHub Copilot

Now that the calculator is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Add a default parameter**

> "Create a power function that takes two parameters, `base` and `exponent`, and returns the base raised to the exponent. Make the exponent default to 2 if not provided."

This prompt demonstrates how to define a function with a **default parameter**. Notice the syntax for setting a default value in the function definition. You can then add this new operation to the menu and test it.

**Return more than one value**

> "Update the divide function to return both the quotient and the remainder when dividing two integers."

This prompt demonstrates how to return multiple values from a function. Notice the syntax for returning a tuple and how to unpack it when calling the function. You can then update the main loop to handle and display both results.

**Use a dictionary to map operations to functions**

> "Refactor the calculator to use a dictionary that maps operation names to their corresponding functions, instead of using if/elif statements."

This is a more advanced prompt that shows how to use a **dictionary** to simplify the code. Instead of multiple `if/elif` statements, you can look up the function in the dictionary and call it directly. This makes the code cleaner and easier to extend with new operations.