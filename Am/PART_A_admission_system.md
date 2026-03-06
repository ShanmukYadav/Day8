# PART A – Student Admission Decision System

## Objective

Build a rule-based admission system evaluating students using academic and non-academic factors.

## Inputs

* Entrance Score
* GPA
* Recommendation letter
* Category
* Extracurricular score

## Category Cutoffs

| Category | Cutoff |
| -------- | ------ |
| General  | 75     |
| OBC      | 65     |
| SC/ST    | 55     |

## Merit Rule

Students scoring **≥95** in entrance exam receive **automatic admission with scholarship**.

## Bonus Points

| Condition             | Bonus |
| --------------------- | ----- |
| Recommendation letter | +5    |
| Extracurricular > 8   | +3    |

## Decision Logic

Effective Score:

```
effective_score = entrance_score + bonus
```

Conditions:

* Scholarship → entrance ≥95
* Regular Admission → score ≥ cutoff and GPA ≥7
* Waitlist → slightly below cutoff
* Rejected → low score or GPA

## Complexity

All operations are constant.

```
Time Complexity: O(1)
```
