class bank_account:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_name = account_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.account_number}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
    
    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number
    def get_account_name(self):
        return self.account_name
    def set_account_name(self, new_name):
        self.account_name = new_name
        print(f"Account name changed to {self.account_name}.")
    def set_account_number(self, new_number):
        self.account_number = new_number
        print(f"Account number changed to {self.account_number}.")


# Example usage
if __name__ == "__main__":
    account = bank_account("123456789", "John Doe", 1000)
    print(f"Account Number: {account.get_account_number()}")
    print(f"Account Name: {account.get_account_name()}")
    print(f"Initial Balance: {account.get_balance()}")

    account.deposit(500)
    account.withdraw(200)
    account.set_account_name("Jane Doe")
    account.set_account_number("987654321")
    print(f"Updated Account Name: {account.get_account_name()}")
    print(f"Updated Account Number: {account.get_account_number()}")