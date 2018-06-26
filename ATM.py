# Let’s represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:
#
# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won’t put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest = 0.1

    def check_balance(self):
        print("The balance for {} is {}.".format(self.name, self.balance))

    def deposit(self, amt):
        self.balance += amt
        print("After a deposit of {}, the balance for {} is {}.".format(amt, self.name, self.balance))

    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            print("After a withdrawl of {}, the balance for {} is {}.".format(amt, self.name, self.balance))
            return self.balance
        print("{}: You do not have enough funds for a withdrawl of {}. Current Balance is {}.".format(self.name, amt, self.balance))

def calculate_interest():
    print("Interest is 0.1%")

# John = BankAccount('John')
# Joe = BankAccount('Joe')
# Guido = BankAccount('Guido')
# print(John.balance)
# John.check_balance()
# John.deposit(24)
# John.withdraw(1)
# calculate_interest()
accounts = {"John": BankAccount('John')}



while True:
    print("Please enter your account information to access your account:")
    user = input(": ")
    if user not in accounts:
        print("Account not found. ")
        new_account = input("Would you like to enter a new account? ")
        if new_account.lower() == "y":
            new_user = input("Enter a new user: ")
            accounts.update({new_user: BankAccount(new_user)})
            print(accounts)
            print("Account for {} has been created. ".format(new_user))
            user = new_user
    else:
        break


while True:
    print("What would you like to do? Enter:")
    print("1 to check balance")
    print("2 to make a deposit")
    print("3 to make a withdrawl")
    print("4 to see your interest rate")
    selection = input(": ")
    if selection == "1":
        accounts[user].check_balance()
    elif selection == "2":
        amt = int(input("How much would you like to deposit? "))
        accounts[user].deposit(amt)
    elif selection == "3":
        amt = int(input("How much would you like to withdraw? "))
        accounts[user].withdraw(amt)
    elif selection == "4":
        calculate_interest()
    else:
        print("Your input is bad. You should feel bad.")
        continue
    another_transaction = input("Would you like to make another transaction? ")
    if another_transaction.lower() != "y":
        print("Goodbye.")
        break
