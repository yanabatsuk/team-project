from main import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, savings_amount):
        # initializing parent class - BankAccount
        super().__init__(customer_name, customer_balance, minimum_balance)
        # additional savings deposit
        self.savings_amount = savings_amount
        savings_amount = 0

    # method to add savings deposit
    def add_savings(self, amount):
        self.savings_amount += amount
        self.customer_balance += amount
        print(f"${amount} added to savings. New savings balance: {self.savings_amount}. Total balance: ${self.customer_balance}.")

    # method to print savings account information
    def print_account_information(self):
        self.print_customer_information()  # calls the inherited method
        print(f"Savings Balance: {self.savings_amount}")