# CheckingAccount.py

from main import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, transfer_limit=1000):
        # Inherit from BankAccount class
        super().__init__(customer_name, customer_balance, minimum_balance)
        self.transfer_limit = transfer_limit  # transfer limit for checking account

    # method withdraw (overriding to include transfer limitation)
    def withdraw(self, amount):
        if amount > self.customer_balance:
            print(f"Insufficient funds! You requested to withdraw ${amount}.")
        elif amount > self.transfer_limit:
            print(f"Transfer limit exceeded! Maximum withdrawal is ${self.transfer_limit}.")
        else:
            super().withdraw(amount)  # Call the base class method to handle withdrawal

    # transfer method (within transfer limit)
    def transfer(self, amount, target_account):
        if amount > self.customer_balance:
            print(f"Insufficient funds! You requested to transfer ${amount}.")
        elif amount > self.transfer_limit:
            print(f"Transfer limit exceeded! Maximum transfer is ${self.transfer_limit}.")
        else:
            self.withdraw(amount)  # Call withdraw method to reduce balance
            target_account.deposit(amount)  # Deposit into target account
            print(f"${amount} transferred to {target_account.customer_name}'s account.")
