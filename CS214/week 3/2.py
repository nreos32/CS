age = float(input("Enter the person's age: "))

if age <= 1:
    print("person is an infant.")
elif age < 13:
    print("person is a child.")
elif age < 20:
    print("person is a teenager.")
else:
    print("person is an adult.")