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

1. Open a browser and navigate to the Python editor at [https://buzahid.github.io/python-coder/app/](https://buzahid.github.io/python-coder/app/).

1. You'll see two panels:
    - **Editor pane** (left): where you write your Python code.
    - **Output terminal** (right): where output is displayed and where you can type input when the program asks for it.

1. The editor may contain some default code. Select all of it and delete it so you're starting with a clean, empty file.

## Display a welcome message

The first thing your program should do is greet the user when it starts. You'll use the `print()` function to display a message on the screen.

1. In the editor pane, type the following code:

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

Now you'll update the program to pause and ask for the user's name. The `input()` function displays a prompt and waits for the user to type a response.

1. Add the following line below your existing code:

    ```python
    name = input("What is your name? ")
    ```

    This line does two things: it displays the prompt `What is your name? ` in the terminal, and it stores whatever the user types into a variable called `name`.

1. Run the program again by selecting **▶**.

1. When `What is your name? ` appears in the output terminal, click on the terminal and type your name, then press **Enter**.

1. The program finishes after you enter your name — but it doesn't say anything yet. You'll fix that in the next step.

## Display a personalized greeting

Now you'll use the `name` variable to build a personalized message. You'll do this with an **f-string** — a string that can embed variable values directly inside it using curly braces `{}`.

1. Add the following line at the end of your code:

    ```python
    print(f"Hello, {name}! It's great to meet you.")
    ```

1. Your complete program should now look like this:

    ```python
    print("Welcome to the greeting program!")
    name = input("What is your name? ")
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

1. Add two more lines below your existing code to ask for a favorite color and include it in a second message:

    ```python
    color = input("What is your favorite color? ")
    print(f"Great choice! {color} is a wonderful color.")
    ```

1. Your complete program should now look like this:

    ```python
    print("Welcome to the greeting program!")
    name = input("What is your name? ")
    print(f"Hello, {name}! It's great to meet you.")
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
> "In Python, how can I print 20 dashes in a row without typing them all out? Can you show me an example?"

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
> "In Python, how can I change a string input to all uppercase, all lowercase, or title case? Can you show me examples of each?"

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

> "In Python, what happens if I try to print a string that contains a quote character inside it? How can I do that without causing an error?"

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
