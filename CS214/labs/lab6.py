basketball_team = {"Michael Jordan", "LeBron James", "Kobe Bryant", "Stephen Curry", "Shaquille O'Neal"}
baseball_team = {"Babe Ruth", "Jackie Robinson", "Derek Jeter", "Mike Trout", "Ken Griffey Jr.", "Barry Bonds", "Hank Aaron", "Willie Mays", "Mickey Mantle"}

soccer_team = {"Lionel Messi", "Cristiano Ronaldo", "LeBron James", "Michael Jordan", "Ken Griffey Jr.", "Derek Jeter", "Neymar Jr.", "Kylian Mbappe", "Robert Lewandowski", "Manuel Neuer", "Sergio Ramos"}

import os

try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    if start >= end:
        print("Error: Start value must be less than end value.")
        exit(1)
    
    print(f"You entered the range: {start} to {end}")
    
    number_range = tuple(range(start, end + 1))
    print(f"Created tuple with range: {number_range}")
    
    even_numbers = tuple([num for num in range(start, end + 1) if num % 2 == 0])
    print(f"Even numbers in the range: {even_numbers}")
    
    squared_numbers = tuple([num**2 for num in range(start, end + 1)])
    print(f"Squared numbers in the range: {squared_numbers}")
    
except ValueError as e:
    print(f"Error: Please enter valid integers: {e}")
    exit(1)

try:
    os.makedirs("data", exist_ok=True)
    print("Data directory checked/created successfully.")
except OSError as e:
    print(f"Error creating data directory: {e}")
    exit(1)

def safe_write_to_file(filename, data_iterable):
    try:
        with open(filename, "w") as file:
            for item in data_iterable:
                file.write(f"{item}\n")
        return True
    except IOError as e:
        print(f"Error writing to {filename}: {e}")
        return False

if (safe_write_to_file("data/basketball_set.txt", basketball_team) and
    safe_write_to_file("data/baseball_set.txt", baseball_team) and
    safe_write_to_file("data/soccer_set.txt", soccer_team)):
    print("Team data written successfully.")
else:
    print("Error occurred while writing team data.")

basketball_soccer_intersection = basketball_team & soccer_team
baseball_soccer_intersection = baseball_team & soccer_team

if (safe_write_to_file("data/intersection_basketball_soccer.txt", basketball_soccer_intersection) and
    safe_write_to_file("data/intersection_baseball_soccer.txt", baseball_soccer_intersection)):
    print("Intersection data written successfully.")
else:
    print("Error occurred while writing intersection data.")

basketball_baseball_union = basketball_team | baseball_team

if safe_write_to_file("data/union_basketball_baseball.txt", basketball_baseball_union):
    print("Union data written successfully.")
else:
    print("Error occurred while writing union data.")

basketball_soccer_difference = basketball_team - soccer_team
baseball_basketball_difference = baseball_team - basketball_team

if (safe_write_to_file("data/difference_basketball_soccer.txt", basketball_soccer_difference) and
    safe_write_to_file("data/difference_baseball_basketball.txt", baseball_basketball_difference)):
    print("Difference data written successfully.")
else:
    print("Error occurred while writing difference data.")

nested_tuple = (1, 2, (3, 4, (5, 6, 7)))
print("\n3-level nested tuple:", nested_tuple)
print("Type of the variable:", type(nested_tuple))
print("First element:", nested_tuple[0])
print("Second element:", nested_tuple[1])
print("Third element (a tuple):", nested_tuple[2])
print("Fourth element (accessing nested tuple):", nested_tuple[2][0])
print("Fifth element (accessing deeply nested tuple):", nested_tuple[2][2][0])

try:
    with open("data/nested_tuple.txt", "w") as file:
        file.write(str(nested_tuple) + "\n")
        file.write("Type: " + str(type(nested_tuple)) + "\n")
        file.write("First element: " + str(nested_tuple[0]) + "\n")
        file.write("Second element: " + str(nested_tuple[1]) + "\n")
        file.write("Third element (a tuple): " + str(nested_tuple[2]) + "\n")
        file.write("Fourth element (accessing nested tuple): " + str(nested_tuple[2][0]) + "\n")
        file.write("Fifth element (accessing deeply nested tuple): " + str(nested_tuple[2][2][0]) + "\n")
    print("Nested tuple has been written to data/nested_tuple.txt")
except IOError as e:
    print(f"Error writing nested tuple to file: {e}")

def flatten_tuple(nested):
    flattened = []
    
    def flatten_helper(item):
        if isinstance(item, tuple):
            for sub_item in item:
                flatten_helper(sub_item)
        else:
            flattened.append(item)
    
    flatten_helper(nested)
    return tuple(flattened)

flattened_tuple = flatten_tuple(nested_tuple)
print("\nFlattened tuple:", flattened_tuple)

try:
    with open("data/flattened_tuple.txt", "w") as file:
        file.write("Original nested tuple: " + str(nested_tuple) + "\n")
        file.write("Flattened tuple: " + str(flattened_tuple) + "\n")
        file.write("\nElements of flattened tuple:\n")
        for i, item in enumerate(flattened_tuple):
            file.write(f"Element {i}: {item}\n")
    print("Flattened tuple has been written to data/flattened_tuple.txt")
except IOError as e:
    print(f"Error writing flattened tuple to file: {e}")

try:
    with open("data/number_range.txt", "w") as file:
        file.write(f"User specified range: {start} to {end}\n")
        file.write(f"Number range tuple: {number_range}\n")
        file.write("\nIndividual elements:\n")
        for i, num in enumerate(number_range):
            file.write(f"Element {i}: {num}\n")
    print("\nNumber range has been written to data/number_range.txt")
except IOError as e:
    print(f"Error writing number range to file: {e}")

try:
    with open("data/even_numbers.txt", "w") as file:
        file.write(f"User specified range: {start} to {end}\n")
        file.write(f"Even numbers tuple: {even_numbers}\n")
        file.write("\nIndividual even numbers:\n")
        for i, num in enumerate(even_numbers):
            file.write(f"Element {i}: {num}\n")
    print("Even numbers have been written to data/even_numbers.txt")
except IOError as e:
    print(f"Error writing even numbers to file: {e}")

try:
    with open("data/squared_numbers.txt", "w") as file:
        file.write(f"User specified range: {start} to {end}\n")
        file.write(f"Squared numbers tuple: {squared_numbers}\n")
        file.write("\nOriginal number -> Squared value:\n")
        for i, num in enumerate(squared_numbers):
            original = i + start
            file.write(f"{original} -> {num}\n")
    print("Squared numbers have been written to data/squared_numbers.txt")
except IOError as e:
    print(f"Error writing squared numbers to file: {e}")

print("All operations completed.")