class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount > self.balance:
            print(f"Insufficient balance. Current balance: ${self.balance:.2f}")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

def show_menu():
    print("\n--- Bank Account Manager ---")
    print("1. Deposit money")
    print("2. Withdraw money") 
    print("3. Check balance")
    print("4. Quit")
    print("----------------------------")

def get_amount(action):
    """Get and validate monetary amount from user input"""
    while True:
        try:
            amount = float(input(f"Enter amount to {action}: $"))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    bank = Bank()
    print("Welcome to your Bank Account!")
    
    while True:
        show_menu()
        
        try:
            choice = input("Select an option (1-4): ").strip()
            
            if choice == '1':
                amount = get_amount("deposit")
                bank.deposit(amount)
                
            elif choice == '2':
                amount = get_amount("withdraw")
                bank.withdraw(amount)
                
            elif choice == '3':
                bank.get_balance()
                
            elif choice == '4':
                print("Thank you for using Bank Account Manager. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nProgram terminated. Goodbye!")
            break

if __name__ == "__main__":
    main()