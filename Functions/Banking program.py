#Python Banking Program

def show_balance():
    pass

def deposit():
    pass

def withdraw():
    pass    

balance = 0
is_logged_in  = True

while is_logged_in:
    print("Welcome to the Banking Program!")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using the Banking Program. Goodbye!")
        is_logged_in = False
    else:
        print("Invalid choice. Please try again.")