from BankAccount import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, savings_balance, interest_rate, account_number, routing_number):
        # initializing parent class - BankAccount
        super().__init__(customer_name, customer_balance, minimum_balance)
        self.savings_balance = savings_balance #savings account balance
        self.interest_rate = interest_rate # interest rate for savings
        self._account_number = account_number # protected number
        self.__routing_number = routing_number # private number


    # method to add savings deposit
    def add_savings(self, amount):
        self.savings_balance += amount
        self.customer_balance += amount
        print(f"${amount} added to {self.customer_name} savings. New savings balance: {self.savings_balance}. Total balance: ${self.customer_balance}.")

    # method to apply interest
    def apply_interest(self):
        interest_earned = self.savings_balance * self.interest_rate
        self.savings_balance += interest_earned
        self.customer_balance += interest_earned
        print(f"Interest of ${interest_earned:.2f} applied. New savings balance: {self.savings_balance}. Total balance: ${self.customer_balance}.")

    # method to print savings account information
    def print_account_information(self):
        self.print_customer_information()  # calls the inherited method
        print(f"Savings Balance: {self.savings_balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")
        print(f"Account Number: {self._account_number}")