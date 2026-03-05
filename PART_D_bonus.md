# Day 8 – Take Home Assignment

## PART D – Bonus Challenge

### Daily Transaction Analyzer (Paytm Case Study)

---

# Problem Statement

You are a backend developer at Paytm building a mini transaction analytics dashboard.

The program should:

1. Accept transactions until the user types `done`
2. Each transaction includes:

   * amount
   * type (credit / debit)
3. Track:

   * total credits
   * total debits
   * net balance
   * number of transactions
4. Flag transactions greater than ₹10,000
5. Print a bar chart of the **last 10 transactions**
6. Display summary statistics

---

# Approach

### Input System

A `while` loop is used to continuously accept transactions until the user enters:

```
done
```

Each transaction stores:

```
(amount, type)
```

in a list.

---

# Data Tracking

The program tracks:

| Metric              | Description                    |
| ------------------- | ------------------------------ |
| total_credits       | sum of all credit transactions |
| total_debits        | sum of all debit transactions  |
| transaction_count   | total number of transactions   |
| highest_transaction | maximum transaction amount     |

---

# High Value Transactions

If a transaction exceeds:

```
₹10,000
```

the program prints a warning:

```
⚠ High value transaction detected
```

This simulates fraud monitoring in fintech systems.

---

# Bar Chart Visualization

The last **10 transactions** are visualized using stars.

```
* per ₹1000
```

Example

```
₹3000 → ***
₹500 → *
```

This provides a quick visual overview of transaction sizes.

---

# Time Complexity

Let **n = number of transactions**

| Operation          | Complexity |
| ------------------ | ---------- |
| Input processing   | O(n)       |
| Summary statistics | O(n)       |
| Bar chart          | O(10)      |

Overall complexity:

```
O(n)
```

---

# Concepts Used

* while loops
* for loops
* list storage
* conditional logic
* simple analytics
* visualization using loops

---

# File

```
transaction_analyzer.py
```

Contains the implementation of the transaction analytics dashboard.
