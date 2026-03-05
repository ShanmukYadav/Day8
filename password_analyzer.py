import random
import string


# --------------------------------
# PASSWORD ANALYZER FUNCTION
# --------------------------------
def analyze_password(password):
    score = 0
    missing = []

    # LENGTH CHECK
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        missing.append("too short")

    # CHARACTER FLAGS
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # FOR LOOP → iterate characters
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "!@#$%^&*":
            has_special = True

    if has_upper:
        score += 1
    else:
        missing.append("uppercase")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append("special char")

    # REPEATED CHARACTER CHECK
    repeat_ok = True
    count = 1

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count > 2:
                repeat_ok = False
                break
        else:
            count = 1

    if repeat_ok:
        score += 1
    else:
        missing.append("too many repeated chars")

    return score, missing


# --------------------------------
# STRENGTH RATING
# --------------------------------
def get_rating(score):

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"


# --------------------------------
# PASSWORD GENERATOR
# --------------------------------
def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


# --------------------------------
# MAIN PROGRAM
# --------------------------------
def main():

    while True:

        password = input("Enter password: ")

        score, missing = analyze_password(password)

        rating = get_rating(score)

        print(f"Strength: {score}/7 ({rating})")

        if missing:
            print("Missing:", ", ".join(missing))

        if score >= 5:
            print("Password accepted!")
            break
        else:
            print("Try again...\n")

    # PASSWORD GENERATOR
    print("\n--- Password Generator ---")

    length = int(input("Enter desired password length: "))

    generated = generate_password(length)

    print("Generated Password:", generated)

    score, missing = analyze_password(generated)

    rating = get_rating(score)

    print(f"Generated Password Strength: {score}/7 ({rating})")


# RUN PROGRAM
if __name__ == "__main__":
    main()