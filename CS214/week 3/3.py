item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))
item4 = float(input("Enter the price of item 4: "))
item5 = float(input("Enter the price of item 5: "))

subtotal = item1 + item2 + item3 + item4 + item5

sales_tax = subtotal * 0.07

total = subtotal + sales_tax

print("\nSubtotal: $" + format(subtotal, ".2f"))
print("Sales Tax (7%): $" + format(sales_tax, ".2f"))
print("Total: $" + format(total, ".2f"))