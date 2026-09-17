#question 4
item = "Shoe"
price = 48.00
quantity = 6
tax_rate = 0.05

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: {subtotal:.2f}")
print(f"Tax amount: {tax:.2f}")
print(f"Final total: {total:.2f}")