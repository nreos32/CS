def get_valid_ticket_count(ticket_class):
    while True:
        try:
            count = int(input(f"Enter the number of Class {ticket_class} tickets sold: "))
            if count < 0:
                print("Number of tickets cannot be negative. Please try again.")
                continue
            return count
        except ValueError:
            print("Please enter a valid number.")

class_a = get_valid_ticket_count('A')
class_b = get_valid_ticket_count('B')
class_c = get_valid_ticket_count('C')

class_a_income = class_a * 20
class_b_income = class_b * 15
class_c_income = class_c * 10

total_income = class_a_income + class_b_income + class_c_income

print("\nIncome from ticket sales:")
print(f"Class A ({class_a} tickets): ${class_a_income:,.2f}")
print(f"Class B ({class_b} tickets): ${class_b_income:,.2f}")
print(f"Class C ({class_c} tickets): ${class_c_income:,.2f}")
print("-" * 40)
print(f"Total income: ${total_income:,.2f}")