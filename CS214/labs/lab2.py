while True:
    num_elements = int(input("Enter the number of elements: "))
    num_fizz = 0
    num_buzz = 0
    num_fizzbuzz = 0

    for i in range(1, num_elements + 1):
        print(f"iteration {i}:")
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            num_fizzbuzz += 1
        elif i % 3 == 0:
            print("Fizz")            
            num_fizz += 1
        elif i % 5 == 0:
            print("Buzz")
            num_buzz += 1

    print("elements:", num_elements)
    print("Fizz:", num_fizz)
    print("Buzz:", num_buzz)
    print("FizzBuzz:", num_fizzbuzz)

    exit_option = input("Do you want to exit? (yes/no): ")
    if exit_option == "yes":
        break
    
    print("\nStarting new run...\n")