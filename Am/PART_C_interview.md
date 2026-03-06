# PART C – Interview Questions

## Difference Between `elif` and Multiple `if`

### Using multiple `if`

Each condition is evaluated independently.

```
score = 85

if score >= 60:
    print("Pass")

if score >= 80:
    print("Distinction")
```

Output

```
Pass
Distinction
```

### Using `elif`

Only one condition executes.

```
if score >= 80:
    print("Distinction")
elif score >= 60:
    print("Pass")
```

Output

```
Distinction
```

Reason: `elif` prevents evaluation of further conditions once one is true.

---

# Triangle Classification

```python
def classify_triangle(a,b,c):

    if a<=0 or b<=0 or c<=0:
        return "Invalid"

    if a+b<=c or a+c<=b or b+c<=a:
        return "Not a triangle"

    if a==b==c:
        return "Equilateral"

    if a==b or b==c or a==c:
        return "Isosceles"

    return "Scalene"
```

---

# Debug Question

Original Code

```
if score >= 60: grade='D'
if score >= 70: grade='C'
if score >= 80: grade='B'
if score >= 90: grade='A'
```

Problem: multiple `if` overwrite the grade.

Fix:

```
if score >= 90:
    grade='A'
elif score >= 80:
    grade='B'
elif score >= 70:
    grade='C'
else:
    grade='D'
```
