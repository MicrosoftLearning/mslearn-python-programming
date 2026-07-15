---
lab:
    title: 'Create a personalized banner app'
    description: 'Set up a Python project in Visual Studio Code, install a package with pip, and use GitHub Copilot to build a banner app that greets the user.'
    level: 100
    duration: 25
    islab: true
    status: 'released'
---

# Create a personalized banner app

In this exercise, you take everything you set up in this module for a test drive. You create a new Python project in Visual Studio Code, set up a virtual environment, install a package with `pip`, and write a small program that turns the user's name into an eye-catching ASCII banner. Along the way, you practice reading an error message and getting help from GitHub Copilot.

This exercise takes approximately **25** minutes.

## Set up your workspace

You'll write and run your code in Visual Studio Code. The starter code for this exercise lives in a GitHub repository — you'll clone that repo and work inside the folder for this exercise.

1. Open a new **Visual Studio Code** window (**File > New Window**).

1. On the Welcome page, select **Clone Git Repository...** (or open the Command Palette with **Ctrl+Shift+P** and run **Git: Clone**).

1. Paste the following URL and press **Enter**:

    ```
    https://github.com/MicrosoftLearning/mslearn-python-programming.git
    ```

1. When the file selection dialog appears, create a new folder in a convenient location to hold the repo (for example, `mslearn-python`), select it, and click **Select as Repository Destination**.

1. After the clone completes, select **Open** to open the folder in VS Code.

1. In the File Explorer, expand the `Labfiles/03-create-personalized-banner` subfolder and select the `app.py` file. This is where you'll write your code.

## Set up your Python environment

Every Python project should have its own virtual environment so its packages stay separate from your other work.

1. Open the integrated VS Code terminal by selecting **Terminal > New Terminal**. Make sure the terminal is set to your project folder — you should see a path ending in `03-create-personalized-banner`.


1. In the terminal, create a virtual environment named `.venv`:

    ```bash
    python -m venv .venv
    ```

    A new hidden folder called `.venv` appears in the Explorer panel.

1. Activate the environment:

    | Platform | Command |
    |---|---|
    | Windows | `.venv\Scripts\activate` |
    | macOS / Linux | `source .venv/bin/activate` |

    When the environment is active, the terminal prompt starts with `(.venv)`.

2. VS Code should automatically detect the environment and offer to use it as the interpreter.

### Troubleshooting

**Interpreter not detected:** If VS Code doesn't detect the virtual environment:
    - Press **Ctrl+Shift+P** (Windows) or **Cmd+Shift+P** (macOS) to open the Command Palette.
    - Type `Python: Select Interpreter` and select it.
    - Choose the interpreter path that includes `.venv`.

**Script disabled (Windows):** If you see an error saying "script execution is disabled on this system," try the following:

1. Seach for "PowerShell" in the Start menu, right-click it, and select **Run as Administrator**.
2. In the PowerShell window, run:

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    ```
3. Close the PowerShell window and return to VS Code. In the terminal, try activating your virtual environment again.

## Install a package with pip

Python's standard library is powerful, but real projects almost always use third-party packages too. You'll install **pyfiglet** — a small package that turns plain text into ASCII-art banners.

1. With the virtual environment active, run:

    ```bash
    pip install pyfiglet
    ```

    You should see a line like `Successfully installed pyfiglet-...`.

1. Confirm the package is installed:

    ```bash
    pip list
    ```

    You should see `pyfiglet` in the list, alongside `pip` itself.

## Review the starter code

1. In the **Explorer** panel, open `app.py`. The `.py` extension tells VS Code this is a Python file. You'll see the following guiding comments already in place:

    ```python
    # Load the pyfiglet package

    # Ask the user for their name

    # Turn the name into a banner

    # Print a greeting
    ```

    Remember, comments are ignored by Python when the program runs. They just help you organize your code. In the steps that follow, you'll add code beneath each comment.

## Load the package into your program

Installing a package puts the code on your machine. To actually use it in your program, you tell Python to **import** it.

1. Beneath the `# Load the pyfiglet package` comment, add the following line:

    ```python
    import pyfiglet
    ```

    The `import` statement loads the package so you can use the functions inside it.

## Ask the user for their name

1. Beneath the `# Ask the user for their name` comment, add the following lines:

    ```python
    name = input("What is your name? ")
    ```

## Turn the name into a banner

The pyfiglet package has a function called `figlet_format()` that takes a string and returns a big ASCII version of it.

1. Beneath the `# Turn the name into a banner` comment, add the following line:

    ```python
    banner = pyfiglet.figlet_format(name)
    ```

    - `pyfiglet.figlet_format(name)` calls the `figlet_format` function that lives inside the `pyfiglet` package.
    - The **return value** — the finished ASCII banner — is stored in the `banner` variable.

## Print a greeting

Now put it all together and display the banner along with a friendly message.

1. Beneath the `# Print a greeting` comment, add the following lines:

    ```python
    print(banner)
    print(f"Hello, {name.upper()}! Welcome to VS Code.")
    ```

    - `print(banner)` displays the multi-line ASCII banner.
    - `name.upper()` converts the name to uppercase inside the f-string, without changing the original `name` variable.

1. Your complete `app.py` should now look like this:

    ```python
    # Load the pyfiglet package
    import pyfiglet

    # Ask the user for their name
    name = input("What is your name? ")
    name = name.strip()

    # Turn the name into a banner
    banner = pyfiglet.figlet_format(name)

    # Print a greeting
    print(banner)
    print(f"Hello, {name.upper()}! Welcome to VS Code.")
    ```

## Run the program

1. Select the **▶ Run Python File** button in the top-right corner of the editor, or run it from the terminal:

    ```bash
    python app.py
    ```

1. When prompted, type your name and press **Enter**. You should see something like:

    ```output
    What is your name? Ada

       _        _
      / \    __| | __ _
     / _ \  / _` |/ _` |
    / ___ \| (_| | (_| |
   /_/   \_\\__,_|\__,_|

    Hello, ADA! Welcome to VS Code.
    ```

## Read an error message

Errors are a normal part of programming. Learning to read them is one of the most important skills you can build early on.

1. On purpose, change `name.upper()` in the last `print()` line to `nam.upper()` — remove the `e` from `name`:

    ```python
    print(f"Hello, {nam.upper()}! Welcome to VS Code.")
    ```

1. Run the program again. Type your name at the prompt. This time you should see an error at the bottom of the terminal:

    ```output
    Traceback (most recent call last):
      File "app.py", line 11, in <module>
        print(f"Hello, {nam.upper()}! Welcome to VS Code.")
    NameError: name 'nam' is not defined
    ```

1. Read the error carefully. It tells you:
    - **What went wrong** — `NameError: name 'nam' is not defined`.
    - **Where it happened** — `File "app.py", line 11`.

    Python couldn't find a variable called `nam` because you defined it as `name`.

1. Fix the typo by putting the `e` back:

    ```python
    print(f"Hello, {name.upper()}! Welcome to VS Code.")
    ```

1. Run the program one more time to confirm everything works again.

## Display a mood banner with GitHub Copilot

GitHub Copilot can help you build on top of what you already have. You'll use a comment to guide Copilot into adding a farewell banner.

1. At the bottom of your `app.py`, on a new line, type the following comment and press **Enter**:

    ```python
    # Ask the user how they're feeling today and print their answer as a banner
    ```

1. Wait a moment. Copilot should display a suggestion in gray text — something similar to:

    ```python
    feeling = input("How are you feeling today? ")
    print(pyfiglet.figlet_format(feeling))
    ```

1. Press **Tab** to accept the suggestion. If Copilot doesn't offer one, press **Enter** once and start typing `feeling = input(` — the suggestion should appear as you type.

    > [!IMPORTANT]
    > Always **read** what Copilot suggests before you accept it. In this case, the suggestion should use `pyfiglet.figlet_format()` — the same function you already used above. If it suggests something completely different, keep typing to guide it or reject the suggestion and write the line yourself.

1. Run the program one more time and answer both prompts. You should see two banners printed back to back.

## Save your project's dependencies

If you ever share this project — or come back to it on another machine — you'll want a record of which packages it needs. That's what `requirements.txt` is for.

1. In the terminal, run:

    ```bash
    pip freeze > requirements.txt
    ```

1. In the Explorer panel, open the new `requirements.txt` file. You should see a single line similar to:

    ```output
    pyfiglet==1.0.2
    ```

    Anyone who opens your project can now recreate the exact environment with `pip install -r requirements.txt`.

## Extend with GitHub Copilot

Now that the banner app is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Try a different banner font**

> "I'm using the pyfiglet package in Python. How do I display text in a different font?"

The banner currently uses the default pyfiglet font. Ask the AI about the `font` argument for `figlet_format()`, then update your program to display the banner in a different style — `"slant"`, `"big"`, and `"bubble"` are good ones to start with.

**Center your greeting**

> "How can I center a string inside a wider space when I print it?"

Right now the `Hello, ...` line sits flush against the left margin, below a wide banner. Ask the AI about the string `.center()` method, then use it to center your greeting inside a 40-character space so it lines up more nicely.

**Ask Copilot to explain your code**

> Open your `app.py`, select the entire program, and ask Copilot Chat: "Explain what this code does, line by line."

Read Copilot's response carefully and compare it to your own understanding. If any line's explanation surprises you, ask a follow-up question (for example, *"Why do we need `.strip()` on the user's name?"*). Using Copilot as a study partner — not just an autocomplete tool — is one of the fastest ways to build understanding as a beginner.
