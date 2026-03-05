transactions = []

total_credits = 0
total_debits = 0
transaction_count = 0
highest_transaction = 0

print("Enter transactions (type 'done' to finish)\n")

# WHILE LOOP INPUT
while True:

    entry = input("Enter amount or 'done': ")

    if entry.lower() == "done":
        break

    amount = float(entry)

    t_type = input("Type (credit/debit): ").lower()

    transactions.append((amount, t_type))

    transaction_count += 1

    if amount > highest_transaction:
        highest_transaction = amount

    # HIGH VALUE ALERT
    if amount > 10000:
        print("⚠ High value transaction detected")

    if t_type == "credit":
        total_credits += amount
    elif t_type == "debit":
        total_debits += amount

print("\n--- Transaction Bar Chart (Last 10) ---")

last_transactions = transactions[-10:]

# BAR CHART
for amount, t_type in last_transactions:

    stars = int(amount / 1000)

    if stars == 0:
        stars = 1

    print(f"{t_type} ₹{amount}: ", end="")

    for _ in range(stars):
        print("*", end="")

    print()

# SUMMARY
net_balance = total_credits - total_debits

average = 0
if transaction_count > 0:
    average = (total_credits + total_debits) / transaction_count

print("\n--- Summary ---")

print("Total transactions:", transaction_count)
print("Total credits:", total_credits)
print("Total debits:", total_debits)
print("Net balance:", net_balance)
print("Highest transaction:", highest_transaction)
print("Average transaction:", average)