from main import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, savings_amount):
        # initializing parent class - BankAccount
        super().__init__(customer_name, customer_balance, minimum_balance)
        # additional savings deposit
        self.savings_amount = savings_amount
        savings_amount = 0
