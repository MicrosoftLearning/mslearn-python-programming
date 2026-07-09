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

1. Open a browser and navigate to the Python editor at [https://buzahid.github.io/python-coder/app/](https://buzahid.github.io/python-coder/app/).

1. You'll see two panels:
    - **Editor pane** (left): where you write your Python code.
    - **Output terminal** (right): where output is displayed and where you can type responses when the program prompts you.

1. Clear any default code from the editor so you're starting with a clean file.

## Store grades as variables

You'll start by storing a student's subject scores as variables. Each score is a number out of 100.

1. In the editor pane, type the following code:

    ```python
    math_score    = 88.0
    english_score = 76.5
    science_score = 91.0
    history_score = 83.5
    ```

    Each variable holds a **float** — a decimal number. Even though some values like `88.0` could be written as whole numbers, using floats from the start ensures your calculations return accurate decimal results later.

1. Add a `print()` statement to confirm the values are stored correctly:

    ```python
    print("Scores entered:")
    print(f"  Math:    {math_score}")
    print(f"  English: {english_score}")
    print(f"  Science: {science_score}")
    print(f"  History: {history_score}")
    ```

1. Select the **▶ (Play)** button to run the program. You should see:

    ```output
    Scores entered:
      Math:    88.0
      English: 76.5
      Science: 91.0
      History: 83.5
    ```

## Calculate the total and average

Now you'll use arithmetic to add up the scores and calculate the average.

1. Add the following code below your existing print statements:

    ```python
    total = math_score + english_score + science_score + history_score
    num_subjects = 4
    average = total / num_subjects
    ```

1. Add a print statement to display the result:

    ```python
    print(f"\nTotal score:   {total}")
    print(f"Number of subjects: {num_subjects}")
    print(f"Average score: {average}")
    ```

    > **Note**: `\n` inside an f-string adds a blank line before the text, which helps separate sections of output.

1. Run the program. The output should now include:

    ```output
    Total score:   339.0
    Number of subjects: 4
    Average score: 84.75
    ```

## Convert the average to a GPA

GPA is typically reported on a 4.0 scale. You'll convert the percentage average using a simple formula:

$$GPA = \frac{average}{100} \times 4.0$$

1. Add the following line to perform the conversion:

    ```python
    gpa = (average / 100) * 4.0
    ```

1. Display the final GPA, rounded to two decimal places using Python's built-in `round()` function:

    ```python
    print(f"\nStudent GPA:   {round(gpa, 2)} / 4.0")
    ```

1. Run the program. Your complete output should now look like:

    ```output
    Scores entered:
      Math:    88.0
      English: 76.5
      Science: 91.0
      History: 83.5

    Total score:   339.0
    Number of subjects: 4
    Average score: 84.75

    Student GPA:   3.39 / 4.0
    ```

## Accept grades from user input

Hardcoded values are useful for testing, but a real program should accept input from the user. The `input()` function always returns a **string**, so you need to convert it to a `float` before you can use it in calculations.

1. Replace the four hardcoded score variables at the top of your program with `input()` calls that collect scores from the user:

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
    print("Enter scores out of 100 for each subject:\n")
    math_score    = float(input("Math score:    "))
    english_score = float(input("English score: "))
    science_score = float(input("Science score: "))
    history_score = float(input("History score: "))

    print("\nScores entered:")
    print(f"  Math:    {math_score}")
    print(f"  English: {english_score}")
    print(f"  Science: {science_score}")
    print(f"  History: {history_score}")

    total = math_score + english_score + science_score + history_score
    num_subjects = 4
    average = total / num_subjects
    gpa = (average / 100) * 4.0

    print(f"\nTotal score:        {total}")
    print(f"Number of subjects: {num_subjects}")
    print(f"Average score:      {average}")
    print(f"\nStudent GPA:        {round(gpa, 2)} / 4.0")
    ```

1. Run the program. When each prompt appears in the output terminal, click on it, type a score, and press **Enter**.

1. Try entering the same values as before to verify your output matches the hardcoded version:

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
