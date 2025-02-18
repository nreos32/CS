loanpayment = 0.0
insurance = 0.0
gas = 0.0
oil = 0.0
tires = 0.0
maintenance = 0.0

loanpayment = float(input("Enter monthly loan payment: "))
insurance = float(input("Enter monthly insurance payment: "))
gas = float(input("Enter monthly gas payment: "))
oil = float(input("Enter monthly oil payment: "))
tires = float(input("Enter monthly tire payment: "))
maintenance = float(input("Enter monthly maintenance payment: "))

total_monthly = loanpayment + insurance + gas + oil + tires + maintenance
total_annual = total_monthly * 12

print("Total monthly cost: ", total_monthly)
print("Total annual cost: ", total_annual)