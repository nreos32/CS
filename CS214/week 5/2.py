class_a = int(input("Enter the number of Class A tickets sold: "))
class_b = int(input("Enter the number of Class B tickets sold: "))
class_c = int(input("Enter the number of Class C tickets sold: "))

class_a_income = class_a * 20
class_b_income = class_b * 15
class_c_income = class_c * 10

total_income = class_a_income + class_b_income + class_c_income

print("\nIncome from ticket sales:")
print(f"Class A income: ${class_a_income:,.2f}")
print(f"Class B income: ${class_b_income:,.2f}")
print(f"Class C income: ${class_c_income:,.2f}")
print(f"Total income: ${total_income:,.2f}")