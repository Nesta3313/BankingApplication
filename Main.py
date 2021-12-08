from CheckingAccount import CheckingAccount, customer
# customer.deposit= int(input("Enter Deposit Amount: "))
# customer.balance = customer.deposit

start = int(input("Enter 1 for Checking account or 2 for savings account, enter 0 to exit: "))

if start == 0:
    print("Goodbye")

elif start == 1:
    print("Checking Account: Welcome, what would you like to do today? ")
    menu = {1:"Print balance", 2:"Deposit", 3:"Withdraw", 4:"Check minimum balance", 5:"Quit"}
    print(menu)
    entry = int(input("Enter a number to continue: "))
    while 0 < entry <= 5:
        if entry == 1:
            customer.get_balance()
        elif entry == 2:
            customer.get_deposit()
        elif entry == 3:
            customer.get_withdrawal()
        elif entry == 4:
            customer.check_minimum_balance()
        else:
            break
        print("Would you like to perform another operation?")
        decision = input("Enter YES or NO: ")
        if decision.lower() == "yes":
            print(menu)
            entry = int(input("Enter a number to continue: "))
        else:
            break

    print("Goodbye")

elif start == 2:
    print("Savings Account: Welcome, what would you like to do today? ")
    menu = {1:"Print balance", 2:"Deposit", 3:"Withdraw", 4:"Quit"}
    print(menu)
    entry = int(input("Enter a number to continue: "))
    while 0 < entry <= 4:
        if entry == 1:
            customer.get_balance()
        elif entry == 2:
            customer.get_deposit()
        elif entry == 3:
            customer.get_withdrawal()
        else:
            break
        print("Would you like to perform another operation?")
        decision = input("Enter YES or NO: ")
        if decision.lower() == "yes":
            print(menu)
            entry = int(input("Enter a number to continue: "))
        else:
            break
    print("Goodbye")

else:
    print("Unknown value entered")




