# student's full name: Yana Batsuk and Bita Ghaffari
# student id: 801302794
# worked together as partners

from BankAccount import BankAccount
from SavingsAccount import Savings
from CheckingAccount import CheckingAccount

print("\n--- test below! for Original BankAccount file/code Assignment #1 ---")

# Yana's Original BankAccount file/code Assignment #1 Work (start here)
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

# Yana's Original BankAccount file/code Assignment #1 Work (end here)

print("\n--- new test below! for checking account ---")

# Bita's Checking Account Work (start here)
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

# Bita's Checking Account Work (end here)

print("\n--- new test below! for savings account ---")

# Yana's Savings Account Work (start here)
# creating instances of SavingsAccount
savings1 = Savings("Hailey Parker", 25000, 500, 5000, 0.02, "13243546", "908978685")

savings2 = Savings("Joey Waters", 10000, 250, 2500, 0.03, "36475869", "807958732")


#running tests for savings class; with both instances
print("\n--- Savings Account Operations ----")
savings1.print_account_information()
savings1.add_savings(500)
savings1.apply_interest()
print("\n") # for cleaner separation and easier reading the output

savings2.print_account_information()
savings2.add_savings(1000)
savings2.apply_interest()
print("\n") # for cleaner separation and easier reading the output

#showing Final Account Details
print("\n---Final Account Detail (Savings) ----")
savings1.print_account_information()
print("\n") # for cleaner separation and easier reading the output
savings2.print_account_information()
# Yana's Savings Account Work (end here)