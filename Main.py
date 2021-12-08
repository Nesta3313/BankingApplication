from CheckingAccount import CheckingAccount, customer

start = int(input("Enter 1 for Checking account or 2 for savings account, enter 0 to exit: "))
if start == 0:
    print("Goodbye")

elif start == 1:
    print("Welcome, what would you like to do today? ")
    menu = {1:"Get balance", 2:"Deposit", 3:"Withdraw", 4:"Quit"}
    print(menu)
    entry = int(input("Enter a number to continue: "))
    while entry != 4:
        if entry == 1:
            customer.get_balance()
            print("Would you like to perform another operation?")
            input("Enter yes or no")
        elif entry == 2:
            customer.get_deposit()
            print("Would you like to perform another operation?")
        else:
            customer.get_withdrawal()
            print("Would you like to perform another operation?")
    print("Goodbye")

else:
    print("Welcome, what would you like to do today? ")
    menu = {1:"Get balance", 2:"Deposit", 3:"Withdraw", 4:"Quit"}
    print(menu)
    entry = int(input("Enter a number to continue: "))
    while entry != 4:
        if entry == 1:
            customer.get_balance()
            print("Would you like to perform another operation?")
        elif entry == 2:
            customer.get_deposit()
            print("Would you like to perform another operation?")
        else:
            customer.get_withdrawal()
            print("Would you like to perform another operation?")
    print("Goodbye")



