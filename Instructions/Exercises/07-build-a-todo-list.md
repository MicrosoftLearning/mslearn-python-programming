---
lab:
    title: 'Build a to-do list'
    description: 'Write a Python program that saves and loads tasks from a text file so a to-do list persists between runs.'
    level: 100
    duration: 25
    islab: true
    status: 'released'
---

# Build a to-do list

In this exercise, you build a to-do list app that remembers your tasks between runs. You practice opening files safely with the `with` statement, **reading** tasks from a file, and **writing** or **appending** new tasks back to disk.

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

1. In the VS Code file explorer, navigate to the `Labfiles/07-build-a-todo-list` subfolder.

1. Select the `todo.py` file. You'll see a set of guiding comments that act as an outline for your program — each one marks where a specific piece of code belongs:

    ```python
    # Configure the file

    # Load existing tasks

    # Show the menu

    # Run the main program loop

    # Save tasks back to the file
    ```

    Remember, comments are ignored by Python when the program runs. They're just there to help you organize your code. In the steps that follow, you'll add code beneath each comment.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Configure the file and create it if it doesn't exist

Every read or write operation needs a file to point at. You'll store the file name in a variable so you can reuse it. Then you'll open the file in **append mode** — this creates the file if it doesn't already exist, without erasing anything if it does.

1. Beneath the `# Configure the file` comment, add the following lines:

    ```python
    tasks_file = "tasks.txt"

    # Make sure the file exists so the first read doesn't fail
    with open(tasks_file, "a"):
        pass
    ```

    - `tasks_file` holds the file name so you don't have to type it every time.
    - Opening in `"a"` (append) mode creates the file if it's missing. `pass` is a placeholder that does nothing — you're only opening the file to make sure it exists.

1. Select the **▶ Run Python File** button in the top-right corner of the editor, or open the terminal (**Terminal > New Terminal**) and run:

    ```bash
    python todo.py
    ```

    The program should run without errors. You won't see output yet.

## Load existing tasks into a list

To work with the tasks in memory, you'll read them out of the file and into a **list** of strings. Reading and writing files works with strings, so each task becomes one line in the file.

1. Beneath the `# Load existing tasks` comment, add the following lines:

    ```python
    with open(tasks_file, "r") as file:
        tasks = [line.strip() for line in file]

    print(f"Loaded {len(tasks)} task(s) from {tasks_file}.")
    ```

    - `open(tasks_file, "r")` opens the file for **reading**.
    - Iterating over `file` gives you one line at a time. `line.strip()` removes the trailing newline character so the tasks stored in the list are clean.
    - `[... for line in file]` is a **list comprehension** — a compact way to build a list. You'll learn more about them later, but for now, read it as: "for every line in the file, add `line.strip()` to the list."

1. Run the program. Since the file is brand new and empty, you should see:

    ```output
    Loaded 0 task(s) from tasks.txt.
    ```

## Show the menu

You'll give the user four choices: view tasks, add a task, remove a task, or quit. Storing the options in a list makes them easy to display and validate.

1. Beneath the `# Show the menu` comment, add the following lines:

    ```python
    menu_options = ["view", "add", "remove", "quit"]
    ```

    You'll display the menu inside the main loop next, so it reappears after every action.

## Run the main program loop

Now you'll wire everything into a `while` loop so the user can keep working with their tasks until they choose to quit.

1. Beneath the `# Run the main program loop` comment, add the following lines:

    ```python
    while True:
        print("\nWhat would you like to do?")
        for option in menu_options:
            print(f"  - {option}")

        choice = input("\nEnter a choice: ").lower()

        if choice not in menu_options:
            print("That's not a valid option. Try again.")
            continue

        if choice == "quit":
            break

        elif choice == "view":
            if not tasks:
                print("You have no tasks yet.")
            else:
                print("\n--- Your tasks ---")
                for i, task in enumerate(tasks, start=1):
                    print(f"  {i}. {task}")

        elif choice == "add":
            new_task = input("What do you need to do? ")
            tasks.append(new_task)
            print(f"Added: {new_task}")

        elif choice == "remove":
            number = int(input("Which task number should I remove? "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("That task number doesn't exist.")
    ```

    - `enumerate(tasks, start=1)` gives you each task along with a 1-based number, which is friendlier for the user than 0-based indexes.
    - `tasks.pop(number - 1)` removes the task at that position and returns it, so you can display what was removed.

1. Run the program. Try adding two or three tasks, viewing the list, and removing one. Everything works — but if you quit and rerun the program, your tasks are gone. You'll fix that in the next section.

## Save tasks back to the file

To make the tasks persist between runs, you need to write them back to the file after the loop ends. You'll use **write mode** (`"w"`) so the file is rewritten fresh each time — that way removed tasks actually disappear.

1. Beneath the `# Save tasks back to the file` comment (at the very end of your program, **outside** the `while` loop), add the following:

    ```python
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

    print(f"Saved {len(tasks)} task(s) to {tasks_file}. Goodbye!")
    ```

    - `open(tasks_file, "w")` opens the file for **writing** and erases what's there.
    - `.write(task + "\n")` writes each task on its own line. Unlike `print()`, `.write()` doesn't add newlines for you.

1. Your complete program should now look like this:

    ```python
    # Configure the file
    tasks_file = "tasks.txt"

    with open(tasks_file, "a"):
        pass

    # Load existing tasks
    with open(tasks_file, "r") as file:
        tasks = [line.strip() for line in file]

    print(f"Loaded {len(tasks)} task(s) from {tasks_file}.")

    # Show the menu
    menu_options = ["view", "add", "remove", "quit"]

    # Run the main program loop
    while True:
        print("\nWhat would you like to do?")
        for option in menu_options:
            print(f"  - {option}")

        choice = input("\nEnter a choice: ").lower()

        if choice not in menu_options:
            print("That's not a valid option. Try again.")
            continue

        if choice == "quit":
            break

        elif choice == "view":
            if not tasks:
                print("You have no tasks yet.")
            else:
                print("\n--- Your tasks ---")
                for i, task in enumerate(tasks, start=1):
                    print(f"  {i}. {task}")

        elif choice == "add":
            new_task = input("What do you need to do? ")
            tasks.append(new_task)
            print(f"Added: {new_task}")

        elif choice == "remove":
            number = int(input("Which task number should I remove? "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("That task number doesn't exist.")

    # Save tasks back to the file
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

    print(f"Saved {len(tasks)} task(s) to {tasks_file}. Goodbye!")
    ```

1. Run the program. Add a few tasks and then choose `quit`. Now run the program again — you should see something like:

    ```output
    Loaded 3 task(s) from tasks.txt.
    ```

    Your tasks were saved to disk, loaded on startup, and are ready to work with again.

## Extend with GitHub Copilot

Now that the to-do list is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Save tasks as they're added**

> "In Python, what's the difference between opening a file in `\"w\"` mode versus `\"a\"` mode?"

The current program only saves tasks when the user quits — if it crashes first, unsaved tasks are lost. Ask the AI about append mode, then change the `add` option so it writes each new task to the file the moment it's added.

**Handle a missing file gracefully**

> "In Python, how do I handle the error that happens when I try to open a file that doesn't exist?"

Your program uses an "open in append mode" trick to make sure the file exists before reading it. Ask the AI about `try` / `except FileNotFoundError`, then use its answer to replace that trick with a cleaner pattern that starts with an empty list on the very first run.

**Mark tasks as complete**

> "In Python, how can I mark items in a list as done without removing them?"

Right now the only way to clear a task is to delete it. Ask the AI for beginner-friendly ways to mark items as done, then add a `"done"` menu option that flags tasks (for example, by prefixing them with `[x]`) instead of removing them. Don't forget to add `"done"` to `menu_options`.
