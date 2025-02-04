P = float(input("Enter the principal amount deposited: "))
annual_rate_percent = float(input("Enter the annual interest rate (as a percentage): "))
n = int(input("Enter the number of times per year that interest is compounded: "))
t = float(input("Enter the number of years the money is invested: "))

r = annual_rate_percent / 100

A = P * (1 + r/n) ** (n * t)

print("\nThe balance after", t, "years is: $" + format(A, ".2f"))