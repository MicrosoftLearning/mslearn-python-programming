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

In this exercise, you build a to-do list app that remembers your tasks between runs. Some of the code—the menu, the main loop, and the branches that respond to each choice—is already provided for you. In this exercise, you fill in the code that reads tasks from a file and appends new tasks back to disk.

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

1. Select the `todo.py` file. Some of the program is already provided—a `while` loop, a menu, and `if`/`elif`/`else` branches that respond to each choice. Four comments mark the places where you'll add code:

    ```python
    # Create a loop that displays a menu and responds to user input
    while True:
        # Display the menu
        print("\n=== Personal To-Do List ===")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Exit")
        
        # Get the user's choice
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            print("\n--- Current Tasks ---")

            # Open the file in Read mode and read the tasks into a list

                
            # Display the tasks

                
        elif choice == "2":
            new_task = input("\nWhat do you need to do? ")

            # Open the file in Append mode to add to the end of the list

                
            print("Task saved!")
            
        elif choice == "3":
            # Exit the program
            print("\nGoodbye! Stay productive.")
            break 
            
        else:
            # Handle invalid input
            print("\nInvalid choice. Please choose 1, 2, or 3.")
    ```

    Remember, comments are ignored by Python when the program runs. They're only there to guide you. In the steps that follow, you'll add code beneath each comment.

1. Make sure your Python environment is active. You should see a Python version displayed in the bottom status bar. If you see a warning, select it and choose your installed Python interpreter.

## Open the file and read the tasks

When the user chooses `1`, you need to open the file that stores your tasks and load its contents into a list you can loop through. You'll use the `with` statement, which opens the file and automatically closes it when you're done.

1. Beneath the `# Open the file in Read mode and read the tasks into a list` comment, add the following lines:

    ```python
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
    ```

    - `open("tasks.txt", "r")` opens a file called `tasks.txt` in **read mode** (`"r"`).
    - `as file` gives the open file a name you can use inside the `with` block.
    - `file.readlines()` returns a list where each item is one line from the file — perfect for a to-do list.

## Display the tasks

Now that `tasks` is a list of strings, you can loop through it and print each one. When a line is read from a file, it comes with a `\n` newline character at the end—you'll strip that off so the output looks clean.

1. Beneath the `# Display the tasks` comment, add the following lines:

    ```python
            for task in tasks:
                print("- " + task.strip())
    ```

    - `for task in tasks:` loops through each item in the list.
    - `task.strip()` removes whitespace (including the trailing newline) from the start and end of the string.
    - Concatenating `"- "` with the task turns each line into a bulleted item.

## Save a new task to the file

When the user chooses `2`, they'll type a task and it needs to be saved. You'll open the same file in **append mode** (`"a"`), which adds new content to the end without erasing what's already there. As a bonus, append mode also **creates the file** if it doesn't exist yet — so you don't need any special setup on the first run.

1. Beneath the `# Open the file in Append mode to add to the end of the list` comment, add the following lines:

    ```python
            with open("tasks.txt", "a") as file:
                file.write(new_task + "\n")
    ```

    - `"a"` mode opens the file for **appending**. Existing tasks are preserved.
    - `file.write()` doesn't add a newline for you the way `print()` does — that's why you concatenate `"\n"` yourself. Without it, every new task would be squashed onto the same line.

## Test your program

Your program is complete. Time to try it out.

1. Select the **▶ Run Python File** button in the top-right corner of the editor, or open the terminal (**Terminal > New Terminal**) and run:

    ```bash
    python todo.py
    ```

1. Choose `2` and add a task like `Buy groceries`. Add one or two more tasks the same way.

1. Choose `1` to view your tasks. You should see them listed, for example:

    ```output
    --- Current Tasks ---
    - Buy groceries
    - Walk the dog
    - Finish Python exercise
    ```

1. Choose `3` to exit. Then run the program again and choose `1`. Your tasks are still there — because they were saved to `tasks.txt`, they persist between runs.

    > **Tip**: Look for a new file called `tasks.txt` in the `07-build-a-todo-list` folder. Open it — each line is one task, exactly as you'd expect.

## Extend with GitHub Copilot

Now that the to-do list is working, use GitHub Copilot to extend it. Open the Copilot Chat panel in VS Code (**Ctrl+Alt+I**) and try the following prompts.

**Number the tasks when viewing them**

> "How can I number the tasks when I loop through the list?"

The current view prints each task with a dash. Ask Copilot about `enumerate()`, then update the display so tasks appear as `1. Buy groceries` instead of `- Buy groceries`. This makes the list easier to read and will help when you add the next feature.


**Add a "Remove a task" option**

> "Add a fourth option to the menu that allows the user to remove a task by number. The program should read the tasks from the file, display them with numbers, ask the user which task to remove, and then write the updated list back to the file."

This prompt provides Copilot with specific instructions for the new feature. You can also ask Copilot to help you with smaller pieces of code, like reading from a file, writing to a file, or displaying a numbered list. When Copilot completes the prompt, try running the program and removing a task. 
