class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

class Account:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, target_account, amount):
        if self != target_account:
            if 0 < amount <= self.balance:
                self.balance -= amount
                target_account.balance += amount
                self.transaction_history.append(f"Transferred ${amount} to {target_account.user.user_id}")
                target_account.transaction_history.append(f"Received ${amount} from {self.user.user_id}")
            else:
                print("Invalid transfer amount or insufficient funds.")
        else:
            print("Cannot transfer to the same account.")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

class ATM:
    def __init__(self, accounts):
        self.accounts = accounts
        self.current_user = None

    def authenticate_user(self, user_id, pin):
        for account in self.accounts:
            if account.user.user_id == user_id and account.user.pin == pin:
                self.current_user = account
                return True
        return False

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.current_user.show_transaction_history()
            elif choice == "2":
                amount = float(input("Enter the withdrawal amount: $"))
                self.current_user.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter the deposit amount: $"))
                self.current_user.deposit(amount)
            elif choice == "4":
                target_id = input("Enter the target user ID for the transfer: ")
                target_account = None
                for account in self.accounts:
                    if account.user.user_id == target_id:
                        target_account = account
                        break
                if target_account:
                    amount = float(input("Enter the transfer amount: $"))
                    self.current_user.transfer(target_account, amount)
                else:
                    print("Target account not found.")
            elif choice == "5":
                print("Thank you for visiting!\nGoodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Create user accounts
    user1 = User("user1", "1234")
    user2 = User("user2", "5678")
    account1 = Account(user1, 1000.0)
    account2 = Account(user2, 500.0)
    accounts = [account1, account2]

    atm = ATM(accounts)

    while True:
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")

        if atm.authenticate_user(user_id, pin):
            print("Authentication successful. Welcome!")
            atm.main_menu()
        else:
            print("Authentication failed. Please try again.")
