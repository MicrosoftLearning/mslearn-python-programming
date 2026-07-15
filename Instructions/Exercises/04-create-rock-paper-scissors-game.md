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

1. In the VS Code file explorer, navigate to the `Labfiles/04-create-rock-paper-scissors-game` subfolder.

1. Select the `game.py` file. 
   
   Because part of this program uses an `if`/`else` block, the starter code includes that structure with comment placeholders inside each branch — so you always know exactly where to add each piece of code.

    ```python
    import random

    # Display the game title

    # Get and display the player's choice

    # Check if the player's choice is invalid

        # Display an invalid input message

    # Play the game if the player's choice is valid

        # Generate the computer's choice

        # Determine the winner
    ```

    > **Note**: Be sure to maintain the correct indentation levels as you add code.

    In the steps that follow, you'll fill in each comment with the corresponding logic.

2. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Display the game title

1. Beneath the `# Display the game title` comment, add the following lines:

    ```python
    print("Rock, Paper, Scissors!")
    print("-" * 23)
    ```

1. Select the **▶ Run Python File** button in the top-right corner, or open the terminal (**Terminal > New Terminal**) and run:

    ```bash
    python game.py
    ```

1. Verify the output:

    ```output
    Rock, Paper, Scissors!
    -----------------------
    ```

## Get the player's choice

1. Beneath the `# Get and display the player's choice` comment, add the following lines:

    ```python
    player = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"You chose: {player}")
    ```

    The `.lower()` method converts whatever the player types to lowercase, so `Rock`, `ROCK`, and `rock` are all treated the same way.

1. Run the program, type a choice when prompted, and verify the output:

    ```output
    Rock, Paper, Scissors!
    -----------------------
    Enter your choice (rock, paper, scissors): Rock
    You chose: rock
    ```

## Validate the player's input

Now you'll replace the placeholder `if` condition with the real validation check. You'll use comparison operators and the `and` logical operator to confirm the player entered a valid choice.

1. Beneath the `# Check if the player's choice is invalid` comment, add the following line:

    ```python
    if player != "rock" and player != "paper" and player != "scissors":
    ```

    The `and` operator ensures the error message only shows if the input matches *none* of the valid options.

2. Beneath the `# Display an invalid input message` comment, add:

    ```python
    print("Invalid choice. Please enter rock, paper, or scissors.")
    ```

    Be sure to maintain the correct indentation levels beneath the `if` statement.

3. Run the program and test it with an invalid entry such as `lizard`:

    ```output
    Enter your choice (rock, paper, scissors): lizard
    You chose: lizard
    Invalid choice. Please enter rock, paper, or scissors.
    ```

4. Run it again with a valid choice to confirm no error appears.

## Generate the computer's choice

The computer needs to pick at random. Python includes a built-in `random` module with a `choice()` function that selects a random item from a list — that `import random` line at the top of your file loads it.

1. First, add an `else` block beneath the comment `# Play the game if the player's choice is valid`.

    ```python
    else:
    ```

    This ensures the computer only picks a choice if the player entered a valid one.

2. Beneath the `# Generate the computer's choice` comment (inside the `else` block), add the following lines:

    ```python
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer}")
    ```

    Be sure to maintain the correct indentation levels beneath the `else` statement.

3. Run the program a few times with a valid choice and observe that the computer's choice changes each time.

## Determine the winner

Now you'll add the game logic inside the `else` block. You'll use `if`/`elif`/`else` with the `==` comparison operator and `and` to check every winning condition.

1. Beneath the `# Determine the winner` comment (inside the `else` block), add the following lines:

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

    # Display the game title
    print("Rock, Paper, Scissors!")
    print("-" * 23)

    # Get and display the player's choice
    player = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"You chose: {player}")

    # Check if the player's choice is invalid
    if player != "rock" and player != "paper" and player != "scissors":
        # Display an invalid input message
        print("Invalid choice. Please enter rock, paper, or scissors.")

    # Play the game if the player's choice is valid
    else:
        # Generate the computer's choice
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer}")

        # Determine the winner
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
