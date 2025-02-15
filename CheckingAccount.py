# CheckingAccount.py
from BankAccount import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, transfer_limit=1000):
        # Initialize parent class
        super().__init__(customer_name, customer_balance, minimum_balance)
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member
        self.transfer_limit = transfer_limit  # Transfer limit for checking account

    # Method to withdraw (overriding to include transfer limitation)
    def withdraw(self, amount):
        if amount > self.customer_balance:
            print(f"Insufficient funds! You requested to withdraw ${amount}.")
        elif amount > self.transfer_limit:
            print(f"Transfer limit exceeded! Maximum withdrawal is ${self.transfer_limit}.")
        else:
            return super().withdraw(amount)  # Ensure balance updates

    # Method to transfer money within transfer limit
    def transfer(self, amount, target_account):
        if amount > self.customer_balance:
            print(f"Insufficient funds! You requested to transfer ${amount}.")
        elif amount > self.transfer_limit:
            print(f"Transfer limit exceeded! Maximum transfer is ${self.transfer_limit}.")
        else:
            self.withdraw(amount)  # Deduct from checking balance
            target_account.deposit(amount)  # Deposit into target account
            print(f"${amount} transferred to {target_account.customer_name}'s account.")

    # Method to display account information
    def print_account_information(self):
        self.print_customer_information()  # Call parent class method
        print(f"Checking Account Number: {self._account_number}")
