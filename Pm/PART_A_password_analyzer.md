# Day 8 – Take Home Assignment

## PART A – Password Strength Analyzer & Generator

### Problem Statement

Build a Python program that:

1. Analyzes password strength
2. Ensures strong password criteria
3. Uses loops (`for`, `while`)
4. Generates secure passwords

---

# Design Thinking / Approach

### 1. Password Strength Evaluation

The password is evaluated using the following criteria:

| Criteria                              | Points |
| ------------------------------------- | ------ |
| Length ≥ 8                            | +1     |
| Length ≥ 12                           | +2     |
| Length ≥ 16                           | +3     |
| Contains uppercase letter             | +1     |
| Contains lowercase letter             | +1     |
| Contains digit                        | +1     |
| Contains special character (!@#$%^&*) | +1     |
| No character repeated more than twice | +1     |

Maximum score: **7+**

---

### 2. Loop Usage

This program intentionally uses loops to practice iteration concepts.

**For Loop**
Used to iterate through each character in the password to check:

* uppercase
* lowercase
* digit
* special character

**Range Loop**
Used to check repeated characters.

**While Loop**
Keeps asking the user to enter a password until the strength score is **≥ 5**.

---

### 3. Strength Rating System

| Score | Rating      |
| ----- | ----------- |
| 0 – 2 | Weak        |
| 3 – 4 | Medium      |
| 5 – 6 | Strong      |
| 7+    | Very Strong |

---

### 4. Password Generator

A random password generator is implemented using:

* `random.choice()`
* Character pool:

```
string.ascii_letters + string.digits + string.punctuation
```

The generated password is also analyzed using the same strength analyzer.

---

# Time Complexity

Password analysis requires scanning the string once.

**Time Complexity:**
O(n)

Where **n = length of password**

This is efficient because each character is visited only once.

---

# Key Python Concepts Used

* for loops
* while loops
* break
* conditionals
* string iteration
* random module
* basic algorithmic checks

---

# Files

`password_analyzer.py`
Contains the full implementation of the analyzer and generator.
