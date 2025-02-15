# student full name: Yana Batsuk
# student id: 801302794
# who did you work with? I worked by myself.


# class named BankAccount
from CheckingAccount import CheckingAccount
class BankAccount:
    # class attribute
    bank_title = "Bank of the Cross"

    def __init__(self, customer_name, customer_balance, minimum_balance):
        # instance variables given to use
        self.customer_name = customer_name
        self.customer_balance = customer_balance
        self.minimum_balance = minimum_balance

    # method deposit
    def deposit(self, amount):
        # add money into the account
        self.customer_balance += amount

    # method withdraw
    def withdraw(self, amount):
        # added validation
        """ if the proposed withdraw causes the balance to go below the minimum balance needed to stay in the account, an error message will be printed that withdraw is denied"""
        if self.customer_balance - amount < self.minimum_balance:
            print(f"Withdraw Denied! Requested withdraw of ${amount} surpasses the minimum balance of ${self.minimum_balance} required for {self.customer_name} account.")
        else:
            # take money out of the account, since it does not pass the minimum balance needed to stay in the account
            self.customer_balance -= amount
            print(f"Withdraw Approved! ${amount} was withdrawn from {self.customer_name}'s account. New balance is ${self.customer_balance}.")

    # method print_customer_information
    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer: {self.customer_name}")
        print(f"Balance: {self.customer_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")

# creating the at least two instances that are need, to make sure the class works
bank_account1 = BankAccount("Josiah Joel", 40321, 25000)
bank_account2 = BankAccount("Alecia Atkins", 53025, 50000)

print("\n") # for cleaner separation and easier reading the output

#testing bank_account1
bank_account1.print_customer_information()
bank_account1.deposit(75)
bank_account1.withdraw(25000) # should invoke the error message
bank_account1.withdraw(100)

print("\n\n") # for cleaner separation and easier reading the output

#testing bank_account2
bank_account2.print_customer_information()
bank_account2.deposit(1000)
bank_account2.withdraw(500)
bank_account2.withdraw(10000) # should invoke the error message


# Creating instances of CheckingAccount
checking1 = CheckingAccount("Emily Johnson", 5000, 100, "987654321", "123456789", 2000)
checking2 = CheckingAccount("Michael Smith", 3000, 50, "567890123", "987654321", 1500)

# Running tests for CheckingAccount class
print("\n--- Checking Account Operations ---")

# Display account details
checking1.print_account_information()
checking2.print_account_information()

# Performing transactions
print("\nPerforming transactions...\n")

# Emily withdraws $600
checking1.withdraw(600)

# Michael withdraws $4000 (exceeds balance)
checking2.withdraw(4000)

# Emily transfers $1500 to Michael
checking1.transfer(1500, checking2)

# Show final account details
print("\n--- Final Account Details ---")
checking1.print_account_information()
checking2.print_account_information()


