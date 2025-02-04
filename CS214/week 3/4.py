shares_purchased = 2000
purchase_price_per_share = 40.00
commission_rate = 0.03

total_purchase = shares_purchased * purchase_price_per_share
purchase_commission = total_purchase * commission_rate

shares_sold = 2000
sale_price_per_share = 42.75

total_sale = shares_sold * sale_price_per_share
sale_commission = total_sale * commission_rate

net_amount = total_sale - sale_commission - (total_purchase + purchase_commission)

print("Amount paid for the stock: $" + format(total_purchase, ".2f"))
print("Commission paid on purchase: $" + format(purchase_commission, ".2f"))
print("Amount for which the stock was sold: $" + format(total_sale, ".2f"))
print("Commission paid on sale: $" + format(sale_commission, ".2f"))
print("Net profit/loss: $" + format(net_amount, ".2f"))

if net_amount > 0:
    print("Joe made a profit.")
elif net_amount < 0:
    print("Joe lost money.")
else:
    print("Joe broke even.")