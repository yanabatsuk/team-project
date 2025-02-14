from main import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, savings_balance, interest_rate, account_number, routing_number):
        # initializing parent class - BankAccount
        super().__init__(customer_name, customer_balance, minimum_balance)
        self.savings_balance = savings_balance #saving
        self.interest_rate = interest_rate
        self.account_number = account_number
        self.routing_number = routing_number


    # method to add savings deposit
    def add_savings(self, amount):
        self.savings_balance += amount
        self.customer_balance += amount
        print(f"${amount} added to savings. New savings balance: {self.savings_balance}. Total balance: ${self.customer_balance}.")

    # method to print savings account information
    def print_account_information(self):
        self.print_customer_information()  # calls the inherited method
        print(f"Savings Balance: {self.savings_balance}")