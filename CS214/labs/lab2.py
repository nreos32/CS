while True:
    try:
        num_elements = int(input("Enter the number of elements: "))
        if num_elements <= 0:
            print("Please enter a positive number.")
            continue

        num_fizz = 0
        num_buzz = 0
        num_fizzbuzz = 0

        for i in range(1, num_elements + 1):
            if i % 3 == 0 and i % 5 == 0:
                num_fizzbuzz += 1
            elif i % 3 == 0:
                num_fizz += 1
            elif i % 5 == 0:
                num_buzz += 1

        print (f"the code looped {num_elements} times.")
        print (f"there are {num_fizz} Fizz, {num_buzz} Buzz, and {num_fizzbuzz} FizzBuzz numbers.")
        
        continue_program = input("Would you like to exit? (yes/no): ").lower()
        if continue_program == 'yes':
            break
            
    except ValueError:
        print("Please enter a valid number.")