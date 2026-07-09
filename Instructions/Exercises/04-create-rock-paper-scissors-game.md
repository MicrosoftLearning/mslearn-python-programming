---
lab:
    title: 'Create a rock, paper, scissors game'
    description: 'Build a rock, paper, scissors game in Python that uses comparison operators, if/elif/else conditional logic, and logical operators to determine the winner.'
    level: 100
    duration: 30
    islab: true
    status: 'released'
---

# Create a rock, paper, scissors game

In this exercise, you build a rock, paper, scissors game in Python. The player types their choice, the computer picks one at random, and your program uses conditional logic to decide who wins. You practice using comparison operators, `if`/`elif`/`else` statements, and logical operators (`and`, `or`, `not`).

This exercise takes approximately **30** minutes.

## Set up your workspace

You'll write and run your code in Visual Studio Code.

1. Open **Visual Studio Code**.

1. Select **File > Open Folder**, create a new folder called `rock-paper-scissors` somewhere on your machine, and open it.

1. In the **Explorer** panel, select the **New File** icon and name the file `game.py`.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Get the player's choice

The first thing your program needs to do is ask the player to choose rock, paper, or scissors.

1. In `game.py`, type the following code:

    ```python
    print("Rock, Paper, Scissors!")
    print("-" * 23)

    player = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"You chose: {player}")
    ```

    The `.lower()` method converts whatever the player types to lowercase, so `Rock`, `ROCK`, and `rock` are all treated the same way.

1. Select the **▶ Run Python File** button in the top-right corner of the editor, or open the terminal (**Terminal > New Terminal**) and enter the command:

    ```bash
    python game.py
    ```

1. Type a choice when prompted and verify the output:

    ```output
    Rock, Paper, Scissors!
    -----------------------
    Enter your choice (rock, paper, scissors): Rock
    You chose: rock
    ```

## Validate the player's input

Before picking a winner, you should check that the player entered a valid choice. You'll use a comparison operator and logical operators to do this.

1. Add the following code below your existing lines:

    ```python
    if player != "rock" and player != "paper" and player != "scissors":
        print("Invalid choice. Please enter rock, paper, or scissors.")
    else:
        print("Valid choice!")
    ```

    The `and` operator ensures the error message only shows if the input matches *none* of the valid options.

1. Run the program and test it with an invalid entry such as `lizard`:

    ```output
    Enter your choice (rock, paper, scissors): lizard
    You chose: lizard
    Invalid choice. Please enter rock, paper, or scissors.
    ```

1. Run it again with a valid choice to confirm the `else` branch works.

## Generate the computer's choice

The computer needs to pick at random. Python includes a built-in `random` module with a `choice()` function that selects a random item from a list.

1. Add the following line at the **very top** of your file, before any other code:

    ```python
    import random
    ```

    This line loads the `random` module so your program can use it. You'll learn more about modules and imports in a later module — for now, treat this as a built-in tool you can call on.

1. Inside the `else` block (replace `print("Valid choice!")` with these lines), generate and display the computer's pick:

    ```python
    else:
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer}")
    ```

1. Your complete program so far should look like this:

    ```python
    import random

    print("Rock, Paper, Scissors!")
    print("-" * 23)

    player = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"You chose: {player}")

    if player != "rock" and player != "paper" and player != "scissors":
        print("Invalid choice. Please enter rock, paper, or scissors.")
    else:
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer}")
    ```

1. Run the program a few times with a valid choice and observe that the computer's choice changes each time.

## Determine the winner

Now you'll add the game logic. You'll use `if`/`elif`/`else` with the `==` comparison operator and `and` to check every winning condition.

1. Add the following code inside the `else` block, below the computer choice line:

    ```python
        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win! Rock crushes scissors.")
        elif player == "paper" and computer == "rock":
            print("You win! Paper covers rock.")
        elif player == "scissors" and computer == "paper":
            print("You win! Scissors cuts paper.")
        else:
            print(f"Computer wins! {computer.capitalize()} beats {player}.")
    ```

    Each `elif` uses `and` to check two conditions at once: both the player's choice *and* the computer's choice must match for that branch to run.

1. Your complete `game.py` should now look like this:

    ```python
    import random

    print("Rock, Paper, Scissors!")
    print("-" * 23)

    player = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"You chose: {player}")

    if player != "rock" and player != "paper" and player != "scissors":
        print("Invalid choice. Please enter rock, paper, or scissors.")
    else:
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win! Rock crushes scissors.")
        elif player == "paper" and computer == "rock":
            print("You win! Paper covers rock.")
        elif player == "scissors" and computer == "paper":
            print("You win! Scissors cuts paper.")
        else:
            print(f"Computer wins! {computer.capitalize()} beats {player}.")
    ```

1. Run the program several times to test each possible outcome — win, lose, and tie.

    ```output
    Rock, Paper, Scissors!
    -----------------------
    Enter your choice (rock, paper, scissors): rock
    You chose: rock
    Computer chose: scissors
    You win! Rock crushes scissors.
    ```

## Extend with GitHub Copilot

Now that the game is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Explore other ways to write conditions**

> "In Python, what is the 'in' operator, and how could I use it to simplify checking if a player's input is valid?"

Python has a cleaner alternative to chaining `!=` with `and`. Ask the AI to explain it and try rewriting your input validation line.

**Understand short-circuit evaluation**

> "What is short-circuit evaluation in Python's 'and' and 'or' operators? Can you show me an example?"

This is an important behavior to understand when your conditions involve function calls or expressions that could raise errors.

**Think about edge cases**

> "What are some edge cases I should test in a rock, paper, scissors game? How could conditional logic handle them?"

Use the AI's answer to think critically about inputs your current program doesn't handle — then decide which ones are worth adding.
