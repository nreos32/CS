x = 4
y = 2
print (x + y)
car_name = "Mercedes"
num_wheels = "4"
print(car_name + " has " + num_wheels + " wheels.")
name = "Nicholas"
num_apples = "24"
num_friends = "7"
print(name + " has " + num_apples + " apples and " + num_friends + " friends.")
bill = "120"
print(num_friends + " people went to eat the bill was " + bill + " dollars. Each person paid " + str(round(int(bill) / int(num_friends), 2)) + " dollars ")
bill_total = float(bill)
num_people = int(num_friends)
cost_per_person = bill_total / num_people
print(f"{num_people} people went to eat. The bill was ${bill_total:.2f}. Each person paid ${cost_per_person:.2f} dollars")
print(f"{num_people} people went to eat. The bill was ${int(bill_total)}. Each person paid ${int(cost_per_person)} dollars")
dessert_cost = 6.55
total_cost_of_desserts = dessert_cost * num_people
print(f"For {num_people} people, with dessert cost of ${dessert_cost:.2f} each, the total cost of desserts is ${total_cost_of_desserts:.2f}")