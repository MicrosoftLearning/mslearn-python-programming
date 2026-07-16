---
lab:
    title: 'Create a Guess the Number game'
    description: 'Write a Python program that uses a while loop, conditional logic, and break to run an interactive Guess the Number game.'
    level: 100
    duration: 25
    islab: true
    status: 'released'
---

# Create a Guess the Number game

In this exercise, you build a classic Guess the Number game. The computer picks a secret number, and the player keeps guessing until they get it right. You practice using a `while` loop to repeat actions, `if/elif/else` to compare values, and `break` to exit the loop when the player wins.

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

1. In the VS Code file explorer, navigate to the `Labfiles/05-create-guess-the-number-game` subfolder.

1. Select the `game.py` file. You'll see a set of guiding comments that act as an outline for your program — each one marks where a specific piece of code belongs:

    ```python
    # Add dependencies


    # Set up the game

    # Ask the player to guess

        # Check the guess and give feedback

    # Announce the result
    ```

    Remember, comments are ignored by Python when the program runs. They're just there to help you organize your code. In the steps that follow, you'll add code beneath each comment.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Pick a secret number

Every guessing game needs a target. You'll use Python's built-in `random` module to pick a random whole number between 1 and 20.

1. Under the `# Add dependencies` comment, add the following line:

    ```python
    import random
    ```


1. Beneath the `# Set up the game` comment, add the following lines:

    ```python
    secret_number = random.randint(1, 20)
    max_guesses = 5
    guess_count = 0

    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {max_guesses} guesses. Good luck!")
    ```

    - `random.randint(1, 20)` returns a random whole number **including** both 1 and 20.
    - `max_guesses` and `guess_count` will control how the loop runs.

1. Select the **▶ Run Python File** button in the top-right corner of the editor, or open the terminal (**Terminal > New Terminal**) and run:

    ```bash
    python game.py
    ```

    You should see something like:

    ```output
    I'm thinking of a number between 1 and 20.
    You have 5 guesses. Good luck!
    ```

## Ask the player to guess

Next, you'll add a `while` loop that keeps prompting the player until they either run out of guesses or get the answer right. The player's input comes in as a string, so you convert it to an integer.

1. Beneath the `# Ask the player to guess` comment, add the following lines:

    ```python
    while guess_count < max_guesses:
        guess_count += 1
        guess = int(input(f"\nGuess #{guess_count}: "))
    ```

    - `while guess_count < max_guesses:` keeps the loop running until the player has used all their guesses.
    - `guess_count += 1` bumps the count each time through the loop — this is what eventually causes the condition to become `False`.
    - `int(input(...))` reads the player's input and converts it to a whole number in one step.

## Check the guess and give feedback

Now the loop needs to compare the guess to the secret number and tell the player whether they were too high, too low, or exactly right. When they guess right, you use `break` to exit the loop early.

Be sure to maintain the correct indentation levels as you add code beneath the `while` loop.

1. Beneath the `# Check the guess and give feedback` comment, add the following lines:

    ```python
        if guess == secret_number:
            print(f"Correct! You got it in {guess_count} guesses.")
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")
    ```

2. Run the program. Type a guess after each prompt and press **Enter**. You should see something like:

    ```output
    I'm thinking of a number between 1 and 20.
    You have 5 guesses. Good luck!

    Guess 1: 10
    Too low.

    Guess 2: 15
    Too high.

    Guess 3: 12
    Correct! You got it in 3 guesses.
    ```

## Announce the result

Right now, if the player runs out of guesses, the program just ends silently. You'll add a final message after the loop to reveal the secret number when the player loses.

1. Beneath the `# Announce the result` comment, add the following:

    ```python
    else:
        print(f"\nOut of guesses! The number was {secret_number}.")
    ```

    Python's `while` loop supports an `else` block that runs **only if the loop finished naturally** (without hitting `break`). It's a perfect fit for handling the "you lost" case so the player sees the secret number.

2. Your complete program should now look like this:

    ```python
    #  Add dependencies
    import random

    # Set up the game
    secret_number = random.randint(1, 20)
    max_guesses = 5
    guess_count = 0

    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {max_guesses} guesses. Good luck!")

    # Ask the player to guess
    while guess_count < max_guesses:
        guess_count += 1
        guess = int(input(f"\nGuess #{guess_count}: "))

        # Check the guess and give feedback
        if guess == secret_number:
            print(f"Correct! You got it in {guess_count} guesses.")
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

    # Announce the result
    else:
        print(f"\nOut of guesses! The number was {secret_number}.")
    ```

3. Run the program a few times. Try guessing correctly on your first try, and also try running out of guesses on purpose to see the losing message.

## Extend with GitHub Copilot

Now that the game is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Handle invalid input safely**

> "What happens if I use `int(input())` and the user types letters instead of a number? How can I handle that safely as a beginner?"

Right now, if the player types anything that isn't a whole number, the program crashes. Ask the AI to show you how to keep prompting until the player enters a valid number, then apply the pattern to your `guess = int(input(...))` line.

**Remember previous guesses**

> "How can I remember which values a user has already entered so I can warn them if they repeat one?"

The current game doesn't stop the player from wasting a guess on a number they already tried. Ask the AI how to track past guesses and use its answer to add a warning that doesn't count repeat guesses against them.

**Give warmer hints**

> "How can I check whether a number is close to another number? Can you show me an example using `abs()`?"

Currently the game only says "too high" or "too low." Ask the AI how to use `abs()` to detect when a guess is within 2 of the answer, and add a "very close" hint to your feedback logic.
