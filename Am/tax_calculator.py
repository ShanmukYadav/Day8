income = float(input("Enter annual income: "))

standard_deduction = 75000
taxable_income = max(0, income - standard_deduction)

tax = 0

slabs = [
    (300000, 0),
    (700000, 0.05),
    (1000000, 0.10),
    (1200000, 0.15),
    (1500000, 0.20),
    (float('inf'), 0.30)
]

previous_limit = 0

print("\nTax Breakdown")

for limit, rate in slabs:
    if taxable_income > previous_limit:

        taxable = min(taxable_income, limit) - previous_limit
        slab_tax = taxable * rate

        print(f"{previous_limit} - {limit}: {taxable} taxed at {rate*100}% → {slab_tax}")

        tax += slab_tax
        previous_limit = limit

print("\nTotal Tax:", tax)

effective_rate = (tax / income) * 100 if income > 0 else 0
print("Effective Tax Rate:", round(effective_rate,2),"%")