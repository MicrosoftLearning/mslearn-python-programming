---
lab:
    title: 'Benchmark and optimize a sales report generator'
    description: 'Use timeit and cProfile to measure a slow sales report, find the function that causes the delay, and confirm that a better algorithm fixes it.'
    level: 200
    duration: 30
    islab: true
    status: 'released'
---

# Benchmark and optimize a sales report generator

A sales report program works, but it slows down as the number of orders grows. In this exercise, you follow the optimization workflow from this module: measure the whole program, profile it to find the bottleneck, compare the slow code with a faster version, switch to the faster version, and measure again.

This exercise takes approximately **30** minutes.

## Set up your workspace

You write and run your code in Visual Studio Code. The starter code is in a GitHub repository.

> **Tip**: If you already cloned the repository in another exercise, skip to the next section.

1. Open a new **Visual Studio Code** window (**File > New Window**).

1. On the Welcome page, select **Clone Git Repository...**, or open the Command Palette (**Ctrl+Shift+P**) and run **Git: Clone**.

1. Enter the following URL and press **Enter**:

    ```
    https://github.com/MicrosoftLearning/mslearn-python-programming.git
    ```

1. Create a folder for the repository, such as `mslearn-python`, and select **Select as Repository Destination**.

1. When the clone completes, select **Open**.

## Review the starter code

1. In the Explorer pane, open the `Labfiles/10-benchmark-sales-report-performance` folder and open `benchmark.py`.

1. Review the functions:

    | Function | Purpose |
    |---|---|
    | `make_order_ids` | Creates a list of order IDs. IDs 0, 1, and 2 appear twice, so they're duplicates. |
    | `calculate_total` | Adds up the sales amounts. |
    | `find_duplicate_orders_slow` | Finds duplicate order IDs by comparing every ID with every other ID. |
    | `find_duplicate_orders_fast` | Finds duplicate order IDs by checking each ID once. |
    | `build_report` | Builds the report text. It currently calls `find_duplicate_orders_slow`. |

    The `if __name__ == "__main__":` block at the bottom creates 5,000 orders and prints the report. It also contains three comments that describe the measurements you add.

1. Open a terminal (**Terminal > New Terminal**), change to the exercise folder, and run the program:

    ```bash
    cd Labfiles/10-benchmark-sales-report-performance
    python benchmark.py
    ```

    ```output
    Orders: 5003
    Total sales: $125,075.00
    Duplicate order IDs: [0, 1, 2]
    ```

    The report is correct. The question is how long it takes.

## Measure the whole report

A single timing varies from run to run, so you use `timeit` to run the report several times and average the result.

1. Beneath the `# Time three runs of the whole report and print the average per run` comment, add the following lines:

    ```python
    runs = 3
    total_time = timeit.timeit(lambda: build_report(order_ids, sales_amounts), number=runs)
    print(f"Whole report: {total_time / runs:.4f} seconds per run")
    ```

    > [!TIP]
    > As you add code, be sure to maintain the correct indentation. Use the existing comments as a guide, entering the new code at the same level of indentation.

    - `timeit.timeit()` runs a function `number` times and returns the total time in seconds.
    - The `lambda` wraps the call to `build_report` so that `timeit` can run it with its arguments.
    - Dividing by `runs` gives the average time for one run.

1. Run the program. Your time differs, but it's roughly a third of a second:

    ```output
    Orders: 5003
    Total sales: $125,075.00
    Duplicate order IDs: [0, 1, 2]
    Whole report: 0.3384 seconds per run
    ```

    That's your baseline. After you make a change, you compare against this number.

## Profile the report to find the bottleneck

The report runs three steps, and you don't know which one takes the time. Guessing can send you to the wrong place, so you profile the program with `cProfile`.

1. Beneath the `# Profile the whole report and sort the results by time spent in each function` comment, add the following line:

    ```python
    cProfile.run("build_report(order_ids, sales_amounts)", sort="tottime")
    ```

    `cProfile.run()` runs the code in the string and prints how many times each function was called and how long it took. `sort="tottime"` lists the functions that spent the most time first.

1. Run the program and look at the top of the profile output:

    ```output
             5015 function calls in 0.367 seconds

       Ordered by: internal time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.366    0.366    0.366    0.366 benchmark.py:16(find_duplicate_orders_slow)
         5005    0.001    0.000    0.001    0.000 {built-in method builtins.len}
            1    0.000    0.000    0.367    0.367 {built-in method builtins.exec}
            1    0.000    0.000    0.366    0.366 benchmark.py:37(build_report)
    ```

    Your numbers differ, but the pattern is the same. These columns matter most:

    | Column | Meaning |
    |---|---|
    | `ncalls` | How many times the function was called. |
    | `tottime` | Time spent inside the function itself, not counting the functions it calls. |
    | `cumtime` | Time spent in the function and everything it calls. |

    `find_duplicate_orders_slow` has almost all of the `tottime`. It's the bottleneck. Making `calculate_total` faster wouldn't help, because it takes almost no time.

## Compare the slow and fast versions

Now that you know which function to fix, measure it on its own at different data sizes. This shows how each version scales.

1. Beneath the `# Time both duplicate finders at three data sizes and print the results` comment, add the following lines:

    ```python
    for size in [500, 1000, 2000]:
        ids = make_order_ids(size)
        slow = timeit.timeit(lambda: find_duplicate_orders_slow(ids), number=3)
        fast = timeit.timeit(lambda: find_duplicate_orders_fast(ids), number=3)
        print(f"{size:5d} IDs: slow {slow:.4f}s, fast {fast:.4f}s")
    ```

    - The loop builds a list of each size and times both functions on it.
    - Each function runs three times for each size.

1. Run the program. The comparison prints after the profile output:

    ```output
      500 IDs: slow 0.0111s, fast 0.0001s
     1000 IDs: slow 0.0435s, fast 0.0002s
     2000 IDs: slow 0.1878s, fast 0.0003s
    ```

    Each time the number of IDs doubles, the slow version takes about four times longer. That's the O(n²) pattern: it compares every ID with every other ID. The fast version stays under a millisecond because it checks each ID once and uses a set to remember the IDs it has seen. That's an O(n) algorithm.

## Switch to the faster function

You chose the better algorithm because the profile showed where the time goes. Now use it in the report.

1. In `build_report`, beneath the `# Use the faster function to find the duplicate order IDs` comment, update the code to the following:

    ```python
    duplicates = find_duplicate_orders_fast(order_ids)
    ```

    The report now calls `find_duplicate_orders_fast`. The rest of the function stays the same.

1. Run the program and look at the first lines of the output:

    ```output
    Orders: 5003
    Total sales: $125,075.00
    Duplicate order IDs: [0, 1, 2]
    Whole report: 0.0004 seconds per run
    ```

    The report shows the same duplicate order IDs, so the result is unchanged. The time per run drops from about 0.34 seconds to under a millisecond.

1. Look at the profile output. `find_duplicate_orders_slow` no longer appears, and the whole program takes about a millisecond:

    ```output
             5014 function calls in 0.001 seconds
    ```

You measured the program, found the bottleneck with a profiler, compared two algorithms, and confirmed the improvement with the same measurement. Always measure again after a change, to prove that it helped.

## Practice with GitHub Copilot

Use GitHub Copilot to practice reading and extending your measurements. Open Copilot Chat (**Ctrl+Alt+I**). Copilot can make mistakes, so run the program and check each answer against your own results.

1. **Check your reading of the profile.** Enter:

    > "Explain the cProfile output for `benchmark.py` line by line. Which function is the bottleneck, and how do the `tottime` and `cumtime` columns show that?"

    Compare the answer with what you concluded. Does Copilot point to the same function?

1. **Remove the repeated timing code.** Enter:

    > "Write a function `compare_functions(slow_func, fast_func, sizes)` that uses timeit to time two functions at each size and prints the results. Use it to replace the `for` loop at the end of `benchmark.py`."

    Run the program. Do the timings match the ones you saw before?

1. **Add another implementation.** Enter:

    > "Add a third duplicate finder that uses `collections.Counter`. Time all three finders at 2,000 order IDs, and time only the two faster ones at 200,000 order IDs. Tell me the Big O of each."

    Run the program. Does the Big O that Copilot gives match the timings you see? The slowest finder is left out of the larger test on purpose, because it would take a long time at 200,000 IDs.
