# PART E – Smart Transaction Validator

A rule-based fraud detection engine for fintech transactions.

## Blocking Rules

* Amount > ₹50,000
* Daily spending > ₹100,000

## Flag Rules

* Transactions before 6 AM or after 11 PM

## Category Limits

| Category    | Limit  |
| ----------- | ------ |
| Food        | ₹5000  |
| Electronics | ₹30000 |

## Decision Hierarchy

Blocking rules override all other rules.

## Complexity

```
O(1)
```
