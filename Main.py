from CheckingAccount import customer
from SavingsAccount import customer_savings
# customer.deposit= int(input("Enter Deposit Amount: "))
# customer.balance = customer.deposit
from time import sleep

def checking():
    print("Checking Account: Welcome, what would you like to do today? ")
    menu = {1: "Print balance", 2: "Deposit", 3: "Withdraw", 4: "Check minimum balance", 5: "Quit"}
    print(menu)
    entry = int(input("Enter a number to continue: "))
    while entry >= 1 or entry <= 5:
        if entry == 1:
            customer.get_balance()
        elif entry == 2:
            customer.get_deposit()
        elif entry == 3:
            customer.get_withdrawal()
        elif entry == 4:
            customer.check_minimum_balance()
        elif entry == 5:
            break
        else:
            print("Invalid Entry")
        print("Would you like to perform another operation?")
        decision = input("Enter YES or any other button to exit: ")
        if decision.lower() == "yes":
            print(menu)
            entry = int(input("Enter a number to continue: "))
        else:
            break

    print("Goodbye")



def savings():
    print("Savings Account: Welcome, what would you like to do today? ")
    menu = {1: "Print balance", 2: "Deposit", 3: "Withdraw", 4: "Interest", 5:"Quit"}
    print(menu)
    entry = int(input("Enter a number to continue: "))
    while entry >= 1 or entry <= 5:
        if entry == 1:
            customer_savings.get_balance()
        elif entry == 2:
            customer_savings.get_deposit()
        elif entry == 3:
            customer_savings.get_withdrawal()
        elif entry == 4:
            customer_savings.interest()
        elif entry == 5:
            break
        else:
            print("Invalid Entry")
        print("Would you like to perform another operation?")
        decision = input("Enter YES or any other button to exit: ")
        if decision.lower() == "yes":
            print(menu)
            entry = int(input("Enter a number to continue: "))
        else:
            break

    print("Goodbye")



def operation():
    start = int(input("Enter 1 for Checking account or 2 for savings account, enter 0 to exit: "))
    while start >= 0 or start <= 2:
        if start == 0:
            print("Goodbye")
            break
        elif start == 1:
            checking()
            break
        elif start == 2:
            savings()
            break
        else:
            print("Unknown value entered")
            start = int(input("Enter 1 for Checking account or 2 for savings account, enter 0 to exit: "))



















try:
    operation()
except ValueError:
    print("Number expected, String entered")





