# PART B – Progressive Tax Calculator

## Objective

Calculate income tax based on India's **New Tax Regime FY 2024-25**.

## Standard Deduction

```
₹75,000
```

This deduction is subtracted from total income before tax calculation.

## Tax Slabs

| Income Slab | Tax Rate |
| ----------- | -------- |
| 0 – 3L      | 0%       |
| 3 – 7L      | 5%       |
| 7 – 10L     | 10%      |
| 10 – 12L    | 15%      |
| 12 – 15L    | 20%      |
| Above 15L   | 30%      |

## Progressive Taxation

Each portion of income is taxed separately based on its slab.

Example:

Income = ₹12L

* First 3L → 0%
* Next 4L → 5%
* Next 3L → 10%
* Remaining → 15%

## Complexity

```
Time Complexity: O(1)
```

Number of slabs is constant.
