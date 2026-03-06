amount = float(input("Transaction amount: "))
category = input("Category: ").lower()
hour = int(input("Hour (0-23): "))
daily_spent = float(input("Spent today: "))


if amount > 50000:
    print("BLOCKED: exceeds single transaction limit")

elif daily_spent + amount > 100000:
    print("BLOCKED: exceeds daily limit")

elif hour < 6 or hour > 23:
    print("FLAGGED: unusual transaction time")

elif category == "food" and amount > 5000:
    print("FLAGGED: food limit exceeded")

elif category == "electronics" and amount > 30000:
    print("FLAGGED: electronics limit exceeded")

else:
    print("APPROVED")