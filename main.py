# student full name: Yana Batsuk
# student id: 801302794
# who did you work with? my partner, Bita
from BankAccount import BankAccount
from SavingsAccount import Savings

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


# creating instances of SavingsAccount
savings1 = Savings("Hailey Parker", 25000, 500, 5000, 0.02, "13243546", "908978685")
savings2 = Savings("Joey Waters", 10000, 250, 2500, 0.03, "36475869", "807958732")

#running tests for savings class; with both instances
print("\n--- Savings Account Operations")
savings1.print_account_information()
savings1.add_savings(500)
savings1.apply_interest()

savings2.print_account_information()
savings2.add_savings(1000)
savings2.apply_interest()

#showing Final Account Details
savings1.print_account_information()
savings2.print_account_information()