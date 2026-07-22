---
lab:
    title: 'Create a personalized greeting'
    description: 'Write a Python program that uses print(), input(), and f-strings to display a personalized greeting message.'
    level: 100
    duration: 15
    islab: true
    status: 'released'
---

# Create a personalized greeting

In this exercise, you write a Python program that asks for the user's name and displays a personalized greeting. You practice using the `print()` function to display output, the `input()` function to collect user input, and f-strings to format a custom message.

This exercise takes approximately **15** minutes.

## Open the online Python IDE

You'll write and run your code using an online Python editor — no installation required.

1. Open a browser and navigate to the Python editor at [https://aka.ms/python-coder](https://aka.ms/python-coder).

2. You'll see two panels:
    - **Editor pane** (left): where you write your Python code.
    - **Output terminal** (right): where output is displayed and where you can type input when the program asks for it.

3. The editor may contain some default code. Select all of it and delete it so you're starting with a clean, empty file.

## Set up your program

Before writing any logic, you'll paste a set of guiding comments into the editor. These comments act as an outline for your program — each one marks where a specific piece of code belongs.

1. Copy the following comments and paste them into the editor pane:

    ```python
    # Display a welcome message

    # Ask for the user's name

    # Display a personalized greeting

    # Ask for the user's favorite color and extend the greeting
    ```

    Remember, comments are ignored by Python when the program runs. They're just there to help you organize your code.

## Display a welcome message

The first thing your program should do is greet the user when it starts. You'll use the `print()` function to display a message on the screen.

1. In the editor pane, add the following line beneath the `# Display a welcome message` comment:

    ```python
    print("Welcome to the greeting program!")
    ```

1. Select the **▶ (Run Code)** button to run the code.

1. Check the output terminal. You should see:

    ```output
    Welcome to the greeting program!
    ```

    > **Note**: If nothing appears, make sure the code is typed exactly as shown, including the quotes and parentheses.

## Ask for the user's name

Now you'll add code that pauses the program and asks for the user's name. The `input()` function displays a prompt and waits for the user to type a response.

1. Beneath the `# Ask for the user's name` comment, add the following line:

    ```python
    name = input("What is your name? ")
    ```

    This line does two things: it displays the prompt `What is your name? ` in the terminal, and it stores whatever the user types into a variable called `name`.

1. Run the program again by selecting **▶**.

1. When `What is your name? ` appears in the output terminal, click on the terminal and type your name, then press **Enter**.

1. The program finishes after you enter your name — but it doesn't say anything yet. You'll fix that in the next step.

## Display a personalized greeting

Now you'll use the `name` variable to build a personalized message. You'll do this with an **f-string** — a string that can embed variable values directly inside it using curly braces `{}`.

1. Beneath the `# Display a personalized greeting` comment, add the following line:

    ```python
    print(f"Hello, {name}! It's great to meet you.")
    ```

1. Run the program, enter your name when prompted, and press **Enter**.

1. You should see output similar to:

    ```output
    Welcome to the greeting program!
    What is your name? Alex
    Hello, Alex! It's great to meet you.
    ```

## Extend the greeting

Let's make the greeting more personal by also asking for the user's favorite color and including it in the message.

1. Beneath the `# Ask for the user's favorite color and extend the greeting` comment, add the following two lines:

    ```python
    color = input("What is your favorite color? ")
    print(f"Great choice! {color} is a wonderful color.")
    ```

1. Your complete program should now look like this:

    ```python
    # Display a welcome message
    print("Welcome to the greeting program!")

    # Ask for the user's name
    name = input("What is your name? ")

    # Display a personalized greeting
    print(f"Hello, {name}! It's great to meet you.")

    # Ask for the user's favorite color and extend the greeting
    color = input("What is your favorite color? ")
    print(f"Great choice! {color} is a wonderful color.")
    ```

1. Run the program and respond to both prompts.

1. Verify the output matches what you entered. For example:

    ```output
    Welcome to the greeting program!
    What is your name? Alex
    Hello, Alex! It's great to meet you.
    What is your favorite color? Blue
    Great choice! Blue is a wonderful color.
    ```

## Code with AI

Using an AI assistant (like Copilot) is  great way to explore a programming language at your own pace. Try each prompt below, read the response carefully, and test the code examples it gives you in the online editor.

### Discovery 1: Create a decorative border

**AI Prompt:**
```In Python, how can I print 20 dashes in a row without typing them all out? Can you show me an example?```

**After the AI responds:** String repetition is a quick way to draw dividers or format output. Try running any examples the AI gives you in the online editor, and experiment with different characters and lengths.

<details>
<summary>Show answer</summary>
You can use string multiplication to repeat a character multiple times. For example, to print 20 dashes in a row, you can use the following code:

```python
print("-" * 20)
```
</details>

### Discovery 2: Transforming text

**AI Prompt:**
```In Python, how can I change a string input to all uppercase, all lowercase, or title case? Can you show me examples of each?```

***After the AI responds:** Look closely at the code examples it provides. Try modifying your greeting program to use one of these transformations on the user's name or favorite color.

<details>
<summary>Show answer</summary>
You can use the following string methods to transform text:

```python
name = input("What is your name? ")

# Converts to all uppercase
uppercase_name = name.upper()  

# Converts to all lowercase
lowercase_name = name.lower() 

# Converts to title case (first letter of each word capitalized)
titlecase_name = name.title() 
```
</details>

### Discovery 3: Printing punctuation

```In Python, what happens if I try to print a string that contains a quote character inside it? How can I do that without causing an error?```

**After the AI responds:** Pay attention to the different ways it suggests for including quotes in strings. Try each method in the online editor and see how they work.

<details>
<summary>Show answer</summary>
You can include quote characters inside a string by using different types of quotes or by escaping them with a backslash. Here are some examples:

```python
# Using double quotes to include single quotes
print("It's a beautiful day!")

# Using single quotes to include double quotes
print('She said, "Hello!"')

# Escaping quotes with a backslash
print("She said, \"Hello!\"")
```
