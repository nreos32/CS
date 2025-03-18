import json
import os

customer_numbers = ["0001"]
customers = []

# Helper functions for better UI
def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print a formatted header with title"""
    clear_screen()
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)
    print()

class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list=False):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.on_mailing_list = on_mailing_list
    
    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "telephone": self.telephone,
            "customer_number": self.customer_number,
            "on_mailing_list": self.on_mailing_list
        }

def making_new_customer_number():
    new_number = str(int(customer_numbers[-1]) + 1).zfill(4)
    customer_numbers.append(new_number)
    return new_number

def save_data():
    with open("customer_numbers.json", "w") as f:
        json.dump(customer_numbers, f)
    
    customer_data = [customer.to_dict() for customer in customers]
    customer_data.sort(key=lambda x: x["customer_number"])

    with open("customers.json", "w") as f:
        json.dump(customer_data, f, indent=4)

def load_data():
    global customer_numbers, customers
    
    try:
        if os.path.exists("customer_numbers.json"):
            with open("customer_numbers.json", "r") as f:
                customer_numbers = json.load(f)
        
        if os.path.exists("customers.json"):
            with open("customers.json", "r") as f:
                customer_data = json.load(f)
                customers = []
                for data in customer_data:
                    customer = Customer(
                        data["name"],
                        data["address"],
                        data["telephone"],
                        data["customer_number"],
                        data["on_mailing_list"]
                    )
                    customers.append(customer)
    except Exception as e:
        print(f"Error loading data: {e}")
        
    # Create default data if nothing was loaded
    if not customer_numbers:
        customer_numbers = ["0001"]
    if not customers:
        customers.append(Customer(
            "Nicholas Maroudas",
            "No address on file",
            "647-537-3854",
            "0001",
            False
        ))

def main():
    load_data()
    
    print_header("WEEK 9 ASSIGNMENT")
    print("Welcome to Week 9")
    print("\nEnter your Customer Number or type 'sign up' to make a new account: ")
    print("\nIf you forgot your Customer Number, please type 'forgot id'.")
    customer_number = input("> ")
    
    found_customer = None
    for customer in customers:
        if customer.customer_number == customer_number:
            found_customer = customer
            break
            
    if found_customer:
        print_header(f"Welcome, {found_customer.name}")
        print(f"Customer Number: {found_customer.customer_number}")
        print(f"Current Address: {found_customer.address}")
        print(f"Telephone: {found_customer.telephone}")
        print(f"Mailing List Status: {'Subscribed' if found_customer.on_mailing_list else 'Not Subscribed'}")
        print("\nWould you like to update your mailing list status? (yes/no)")
        
        if input("> ").lower().startswith('y'):
            print("\nEnter your address: ")
            address = input("> ")

            if address.strip():
                found_customer.address = address
                found_customer.on_mailing_list = True
                print("\nThank you for signing up for our mailing list!")
                print(f"Weekly flyers will be sent to: {found_customer.address}")
        
        input("\nPress Enter to continue...")
    
    elif customer_number.lower() == "sign up":
        print_header("New Customer Registration")
        print("Please enter your information:")
        print("\nEnter your name: ")
        name = input("> ")
        print("Enter your address (leave blank to skip): ")
        address = input("> ")
        print("Enter your telephone number: ")
        telephone = input("> ")

        new_customer_number = making_new_customer_number()
        new_customer = Customer(name, address, telephone, new_customer_number, False)
        customers.append(new_customer)
        
        print_header("Registration Complete")
        print(f"Welcome, {new_customer.name}!")
        print(f"Your Customer Number is: {new_customer.customer_number}")
        print("\nWould you like to join our mailing list? (yes/no)")
        
        if input("> ").lower().startswith('y'):
            if not address.strip():
                print("\nPlease enter your mailing address: ")
                address = input("> ")
                new_customer.address = address
            
            if new_customer.address.strip():
                new_customer.on_mailing_list = True
                print("\nThank you for signing up for our mailing list!")
                print(f"Weekly flyers will be sent to: {new_customer.address}")
            else:
                print("\nNo address provided. You can update your mailing preferences later.")
        
        input("\nPress Enter to continue...")

    elif customer_number.lower() == "forgot id":
        print_header("Forgot Customer Number")
        print("Please enter your name or phone number: ")
        search_term = input("> ")
        
        search_term = search_term.lower().strip()
        found_matches = []
        
        for customer in customers:
            if (search_term in customer.name.lower() or 
                search_term in customer.telephone.lower()):
                found_matches.append(customer)
                    
            for i, match in enumerate(found_matches, 1):
                print(f"{i}. Name: {match.name}")
                print(f"   Customer Number: {match.customer_number}")
                print(f"   Phone: {match.telephone}")
                print(f"   Address: {match.address}")
                print()
                
            print("\nPlease use your customer number to log in.")
        else:
            print_header("No Matches Found")
            print("Sorry, no matching customers were found.")
            print("Would you like to create a new account? (yes/no)")
            
            if input("> ").lower().startswith('y'):
                print_header("New Customer Registration")
                print("Please enter your information:")
            else:
                print("Please try searching again with different information.")
        
        input("\nPress Enter to continue...")
        
    else:
        print("\nInvalid Customer Number.")
        print("Please try again or type 'sign up' to create a new account.")
        input("\nPress Enter to continue...")
    
    save_data()
    print_header("Thank You")

if __name__ == "__main__":
    main()