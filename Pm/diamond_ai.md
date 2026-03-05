# Day 8 – Take Home Assignment

## PART C – AI Augmented Task

---

# 1. Prompt Used

The following prompt was given to an AI model:

```
Write a Python program that prints a diamond pattern of asterisks.
The user inputs the number of rows for the upper half.
Include proper spacing and use nested loops only (no string multiplication tricks).
```

---

# 2. AI Generated Output

```python
def print_diamond(n):

    # Upper half
    for i in range(1, n + 1):

        for j in range(n - i):
            print(" ", end="")

        for k in range(2 * i - 1):
            print("*", end="")

        print()

    # Lower half
    for i in range(n - 1, 0, -1):

        for j in range(n - i):
            print(" ", end="")

        for k in range(2 * i - 1):
            print("*", end="")

        print()


n = int(input("Enter number of rows: "))
print_diamond(n)
```

---

# 3. Output Example

For input:

```
n = 4
```

Output:

```
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

# 4. Critical Evaluation

### 1. Spacing Correctness

The spacing is handled correctly using:

```
for j in range(n - i)
```

This ensures the stars are centered properly.

However, spacing could break if `n = 0` because the loops would not run.

---

### 2. Readability

The code is reasonably readable:

* Separate loops for upper and lower halves
* Clear variable usage

But improvements could include:

* Adding comments
* Handling invalid input

---

### 3. Edge Cases

The AI code does not handle:

| Case           | Issue                            |
| -------------- | -------------------------------- |
| n = 0          | No output                        |
| n = 1          | Diamond collapses to single star |
| negative input | Not handled                      |

These should ideally be validated.

---

### 4. Nested Loop Requirement

The requirement says **no string multiplication tricks**.

The AI solution correctly uses **nested loops**:

* loop for spaces
* loop for stars

Therefore it satisfies the constraint.

---

### 5. Time Complexity

The algorithm prints approximately:

```
2n - 1 rows
```

Each row prints up to `2n` characters.

Time complexity:

```
O(n²)
```

This is expected for pattern printing problems.

---

# 5. Improved Version

Below is an improved version with better input validation and clearer structure.

```python
def print_diamond(n):

    if n <= 0:
        print("Invalid input")
        return

    # Upper half
    for i in range(1, n + 1):

        for space in range(n - i):
            print(" ", end="")

        for star in range(2 * i - 1):
            print("*", end="")

        print()

    # Lower half
    for i in range(n - 1, 0, -1):

        for space in range(n - i):
            print(" ", end="")

        for star in range(2 * i - 1):
            print("*", end="")

        print()


n = int(input("Enter number of rows: "))
print_diamond(n)
```

---

# Conclusion

The AI generated solution was mostly correct but lacked:

* input validation
* edge case handling
* clear documentation

After minor improvements, the program becomes more robust and easier to maintain.
