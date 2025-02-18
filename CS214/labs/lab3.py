# 1. Create an empty list named nums to store user input
# 2. Request user input to get a number or list of numbers
# 3. Insert number or list of numbers into the nums list
# 4. Ask input from user if they would like to enter another number; if yes get input
# 5. After user has entered all numbers, use a loop to iterate over numbers entered
# 6. Determine largest and smallest number entered by user
# 7. Display list of numbers entered, max number, and minimum number to user

def get_numbers_from_input(input_string):
    numbers = []
    for value in input_string.split():
        try:
            num = int(value)
            numbers.append(num)
        except ValueError:
            print(f"'{value}' is not a valid number - skipping")
    return numbers

nums = []
while True:
    user_input = input("Enter a number or list of numbers with a space between: ")
    if user_input.strip():
        new_numbers = get_numbers_from_input(user_input)
        nums.extend(new_numbers)
    
    user_again = input("Would you like to enter another number? (yes/no) ").lower().strip()
    if user_again == "no":
        break
    elif user_again != "yes":
        print("Invalid input - please enter 'yes' or 'no'. Assuming 'no'.")
        break

print("\nNumbers entered:", nums)
if nums:
    print("Largest number:", max(nums))
    print("Smallest number:", min(nums))
    print("Total numbers entered:", len(nums))
else:
    print("No valid numbers were entered")