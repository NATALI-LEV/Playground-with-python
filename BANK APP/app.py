class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for withdrawal or insufficient funds.")

    def check_balance(self):
        print(f"Account Balance for {self.holder_name}: ${self.balance}")


def main():
    accounts = {}

    while True:
        print("\nBanking Options:")
        print("1. Create an Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            holder_name = input("Enter account holder's name: ")
            accounts[account_number] = BankAccount(account_number, holder_name)
            print(f"Account created for {holder_name} with account number {account_number}.")
        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter the amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter the amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            account_number_from = input("Enter your account number: ")
            account_number_to = input("Enter the recipient's account number: ")
            
            if account_number_from in accounts and account_number_to in accounts:
                amount = float(input("Enter the amount to transfer: "))
                if amount > 0:
                    if accounts[account_number_from].balance >= amount:
                        accounts[account_number_from].withdraw(amount)
                        accounts[account_number_to].deposit(amount)
                        print(f"Transferred ${amount} from account {account_number_from} to account {account_number_to}.")
                    else:
                        print("Insufficient funds for the transfer.")
                else:
                    print("Invalid amount for transfer.")
            else:
                print("One or both of the accounts not found.")
        elif choice == '5':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")
        elif choice == '6':
            print("Exiting the Banking App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
