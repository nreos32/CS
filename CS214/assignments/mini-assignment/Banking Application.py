balance = 1000.00

def display_welcome():
    """Display welcome message to Humber bank terminal"""
    print("\nWelcome to Humber Bank Terminal")

def verify_pin():
    """Verify user PIN with 3 chances"""
    correct_pin = "1234"
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        user_pin = input("\nPlease enter your 4-digit PIN: ")
        
        if not user_pin.isdigit() or len(user_pin) != 4:
            print("Invalid PIN format. PIN must be 4 digits.")
            attempts += 1
        elif user_pin == correct_pin:
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect PIN. You have {remaining} attempts remaining.")
            else:
                print("You have exceeded the maximum number of attempts.")
    
    return False

def display_balance():
    """Display current account balance"""
    global balance
    print(f"\nYour current balance is: ${balance:.2f}")
    
def make_withdrawal():
    """Process a withdrawal transaction"""
    global balance
    
    print("\n--- Withdrawal Menu ---")
    print("1. $20")
    print("2. $40")
    print("3. $60")
    print("4. $80")
    print("5. $100")
    print("6. Custom amount")
    
    choice = input("\nSelect an option (1-6): ")
    
    withdrawal_amounts = {
        "1": 20.00,
        "2": 40.00,
        "3": 60.00,
        "4": 80.00,
        "5": 100.00
    }
    
    withdrawal_amount = 0.00
    
    if choice in withdrawal_amounts:
        withdrawal_amount = withdrawal_amounts[choice]
    elif choice == "6":
        while True:
            try:
                custom_amount = float(input("\nEnter withdrawal amount: $"))
                if custom_amount <= 0:
                    print("Please enter a positive amount.")
                    continue
                withdrawal_amount = custom_amount
                break
            except ValueError:
                print("Please enter a valid amount.")
    else:
        print("Invalid option selected.")
        return
    
    if withdrawal_amount > balance:
        print("\nInsufficient funds. Transaction cancelled.")
        return
    
    balance -= withdrawal_amount
    print(f"\nWithdrawal of ${withdrawal_amount:.2f} successful.")
    print(f"Your new balance is: ${balance:.2f}")

def make_deposit():
    """Process a deposit transaction"""
    global balance
    
    while True:
        try:
            deposit_amount = float(input("\nEnter deposit amount: $"))
            if deposit_amount <= 0:
                print("Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
    
    balance += deposit_amount
    print(f"\nDeposit of ${deposit_amount:.2f} successful.")
    print(f"Your new balance is: ${balance:.2f}")

def display_menu():
    """Display main menu options"""
    print("\n--- Main Menu ---")
    print("1. Check Balance")
    print("2. Make Withdrawal")
    print("3. Make Deposit")
    print("4. Exit")

def main():
    """Main application function"""
    display_welcome()
    
    if not verify_pin():
        print("\nFor security reasons, the program will now exit.")
        return
    
    continue_session = True
    
    while continue_session:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            display_balance()
        elif choice == "2":
            make_withdrawal()
        elif choice == "3":
            make_deposit()
        elif choice == "4":
            print("\nThank you for using Humber Bank Terminal. Goodbye!")
            return
        else:
            print("\nInvalid option. Please try again.")
            continue
        
        another_action = input("\nWould you like to perform another action? (y/n): ").lower()
        if another_action != 'y':
            print("\nThank you for using Humber Bank Terminal. Goodbye!")
            continue_session = False

if __name__ == "__main__":
    main()