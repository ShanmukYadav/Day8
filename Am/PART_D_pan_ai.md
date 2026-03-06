# PART D – AI Augmented Task

## Prompt

```
Write a Python program that validates an Indian PAN card number format using if-else conditions.
PAN format: 5 uppercase letters, 4 digits, 1 uppercase letter.
```

## Improved Python Code

```python
pan = input("Enter PAN: ")

if len(pan) != 10:
    print("Invalid PAN length")

else:
    valid = True

    for i in range(5):
        if not pan[i].isalpha() or not pan[i].isupper():
            valid = False

    for i in range(5,9):
        if not pan[i].isdigit():
            valid = False

    if not pan[9].isalpha():
        valid = False

    if valid:
        print("Valid PAN")
    else:
        print("Invalid PAN")
```

## Evaluation

* Character positions validated
* Handles invalid length
* Uses character-by-character validation instead of regex
