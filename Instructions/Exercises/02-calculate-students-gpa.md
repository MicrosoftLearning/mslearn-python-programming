---
lab:
    title: 'Calculate a student''s GPA'
    description: 'Write a Python program that stores student grades as variables, performs arithmetic to calculate a GPA, and accepts scores as user input using type conversion.'
    level: 100
    duration: 20
    islab: true
    status: 'released'
---

# Calculate a student's GPA

In this exercise, you write a Python program that calculates a student's Grade Point Average (GPA). You practice storing values in variables, performing arithmetic operations, and converting user input from text to numbers so you can use it in calculations.

This exercise takes approximately **20** minutes.

## Open the online Python IDE

1. Open a browser and navigate to the Python editor at [https://microsoftlearning.github.io/python-coder](https://microsoftlearning.github.io/python-coder/).

1. You'll see two panels:
    - **Editor pane** (left): where you write your Python code.
    - **Output terminal** (right): where output is displayed and where you can type responses when the program prompts you.

1. Clear any default code from the editor so you're starting with a clean file.

## Set up your starter code

Before writing any logic, you'll paste a set of guiding comments into the editor. These comments act as an outline for your program — each one marks where a specific piece of code belongs.

1. Copy the following comments and paste them into the editor pane:

    ```python
    # Collect subject scores

    # Display the entered scores

    # Calculate the total, average, and GPA

    # Display the results
    ```

    Remember, comments are ignored by Python when the program runs. They're just there to help you organize your code.

1. Leave the code as-is for now. In the steps that follow, you'll add code beneath each comment.

## Store grades as variables

You'll start by storing a student's subject scores as hardcoded variables. Each score is a number out of 100.

1. Beneath the `# Collect subject scores` comment, add the following lines:

    ```python
    math_score    = 88.0
    english_score = 76.5
    science_score = 91.0
    history_score = 83.5
    ```

    Each variable holds a **float** — a decimal number. Even though some values like `88.0` could be written as whole numbers, using floats from the start ensures your calculations return accurate decimal results later.

1. Beneath the `# Display the entered scores` comment, add the following lines:

    ```python
    print("Scores entered:")
    print(f"  Math:    {math_score}")
    print(f"  English: {english_score}")
    print(f"  Science: {science_score}")
    print(f"  History: {history_score}")
    ```

1. Select the **▶ (Run Code)** button to run the program. You should see:

    ```output
    Scores entered:
      Math:    88.0
      English: 76.5
      Science: 91.0
      History: 83.5
    ```

## Calculate the total, average, and GPA

Now you'll use arithmetic to add up the scores, calculate the average, and convert it to a GPA on a 4.0 scale using the formula:

$$GPA = \frac{average}{100} \times 4.0$$

1. Beneath the `# Calculate the total, average, and GPA` comment, add the following lines of code:

    ```python
    total = math_score + english_score + science_score + history_score
    num_subjects = 4
    average = total / num_subjects
    gpa = (average / 100) * 4.0
    ```

2. Beneath the `# Display the results` comment, add the following lines of code:

    ```python
    print(f"\nTotal score:        {total}")
    print(f"Number of subjects: {num_subjects}")
    print(f"Average score:      {average}")
    print(f"\nStudent GPA:        {round(gpa, 2)} / 4.0")
    ```

    > **Note**: `\n` inside an f-string adds a blank line before the text, which helps separate sections of output. `round(gpa, 2)` rounds the GPA to two decimal places.

3. Run the program. Your complete output should now look like this:

    ```output
    Scores entered:
      Math:    88.0
      English: 76.5
      Science: 91.0
      History: 83.5

    Total score:        339.0
    Number of subjects: 4
    Average score:      84.75

    Student GPA:        3.39 / 4.0
    ```

## Accept grades from user input

Hardcoded values are useful for testing, but a real program should accept input from the user. The `input()` function always returns a **string**, so you need to convert it to a `float` before you can use it in calculations.

1. Replace the four hardcoded score variables beneath the `# Collect subject scores` comment with the following `input()` calls:

    ```python
    print("Enter scores out of 100 for each subject:\n")
    math_score    = float(input("Math score:    "))
    english_score = float(input("English score: "))
    science_score = float(input("Science score: "))
    history_score = float(input("History score: "))
    ```

    Wrapping `input()` inside `float()` converts the text the user types into a decimal number in a single step.

1. Keep the rest of your code exactly as it is. Your complete program should now look like this:

    ```python
    # Collect subject scores
    print("Enter scores out of 100 for each subject:\n")
    math_score    = float(input("Math score:    "))
    english_score = float(input("English score: "))
    science_score = float(input("Science score: "))
    history_score = float(input("History score: "))

    # Display the entered scores
    print("\nScores entered:")
    print(f"  Math:    {math_score}")
    print(f"  English: {english_score}")
    print(f"  Science: {science_score}")
    print(f"  History: {history_score}")

    # Calculate the total, average, and GPA
    total = math_score + english_score + science_score + history_score
    num_subjects = 4
    average = total / num_subjects
    gpa = (average / 100) * 4.0

    # Display the results
    print(f"\nTotal score:        {total}")
    print(f"Number of subjects: {num_subjects}")
    print(f"Average score:      {average}")
    print(f"\nStudent GPA:        {round(gpa, 2)} / 4.0")
    ```

1. Run the program. When each prompt appears in the output terminal, click on it, type a score, and press **Enter**.

2. Try entering the same values as before to verify your output matches the following:

    ```output
    Enter scores out of 100 for each subject:

    Math score:    88
    English score: 76.5
    Science score: 91
    History score: 83.5

    Scores entered:
      Math:    88.0
      English: 76.5
      Science: 91.0
      History: 83.5

    Total score:        339.0
    Number of subjects: 4
    Average score:      84.75

    Student GPA:        3.39 / 4.0
    ```

## Code with AI

Using an AI assistant (like Copilot) is  great way to explore a programming language at your own pace. Try each prompt below, read the response carefully, and test the code examples it gives you in the online editor.

### Discovery 1: Find the sum of a group of numbers

**AI Prompt:**
> "In Python, what's a quick way to find the sum of a group of numbers? Can you show me beginner friendly examples?"

**After the AI responds:** Take a look at the examples the AI gives you. Do you see a way to simplify your total score calculation? Try it out in your program and see if it works as expected.

<details>
<summary>Show answer</summary>
In Python, you can use the built-in `sum()` function to quickly find the sum of a group of numbers. For example, instead of adding each score individually, you can pass a list of scores to `sum()`:

```python
total = sum(math_score, english_score, science_score, history_score)
```

### Discovery 2: Exploring math functions

**AI Prompt:**
> "In Python, what are some common math functions I can use to compare numbers? Can you show me beginner friendly examples?"

**After the AI responds:** Take a look at the examples the AI gives you. Can you find a way to quickly retrieve the highest and lowest scores from your list of grades? Try it out in your program and see if it works as expected.

<details>
<summary>Show answer</summary>
Python has several built-in math functions that can help you compare numbers. For example, you can use `max()` to find the highest value in a group of numbers and `min()` to find the lowest:

```python
highest_score = max(math_score, english_score, science_score, history_score)

lowest_score = min(math_score, english_score, science_score, history_score)
```

### Discovery 3: Controlling decimal precision

**AI Prompt:**
> "In Python, how can I display shortened floats in strings? Can you show me beginner friendly examples?"

**After the AI responds:** Take a look at the examples the AI gives you. Can you find a way to display your average score and GPA without using `round()`? Try it out in your program and see if it works as expected.

<details>
<summary>Show answer</summary>
You can control the number of decimal places displayed in a float by using formatted string literals (f-strings) with format specifiers. For example, to display a float with two decimal places, you can use `:.2f`:

```python
average = 84.756
print(f"Average score: {average:.2f}")  # Output: Average score: 84.76

gpa = 3.394
print(f"Student GPA: {gpa:.2f} / 4.0")  # Output: Student GPA: 3.39 / 4.0
```
