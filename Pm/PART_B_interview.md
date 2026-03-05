# Day 8 – Take Home Assignment

## PART B – Interview Ready

---

# Q1. Conceptual Questions

## 1. Difference Between `break` and `continue`

### `break`

`break` is used to **immediately exit the loop** when a condition is met.

The loop stops executing completely.

### Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output

```
0
1
2
3
4
```

Explanation:
When `i == 5`, the loop terminates and no further iterations occur.

---

### `continue`

`continue` is used to **skip the current iteration** and move to the next iteration of the loop.

### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output

```
0
1
3
4
```

Explanation:
When `i == 2`, that iteration is skipped and the loop continues.

---

### Key Difference

| Feature                   | break | continue |
| ------------------------- | ----- | -------- |
| Stops loop                | Yes   | No       |
| Skips current iteration   | No    | Yes      |
| Loop continues afterwards | No    | Yes      |

---

# 2. `else` Clause in Loops

Python allows an `else` block with `for` and `while` loops.

The `else` block executes **only if the loop finishes normally** and **no `break` statement is triggered**.

---

### Example

```python
for i in range(5):
```
