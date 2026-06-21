#Python Banking Program

def show_balance(balance):
    print("---------------------------------")
    print(f"Your balance is: ${balance:.2f}")
    print("---------------------------------")

def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print("Invalid amount. Please enter a valid amount.")
        return 0 #We return 0 to avoid adding a negative amount to the balance
    else:
        return amount    

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
    elif amount < 0:
        print("Invalid amount. Please enter a valid amount.")  
    else:    
        return amount

def main():
    balance = 0
    is_logged_in = True

    while is_logged_in:
       print("---------------------------------")
       print("Welcome to the Banking Program!")
       print("---------------------------------")
       print("1. Show Balance")
       print("2. Deposit")
       print("3. Withdraw")
       print("4. Exit")

       choice = input("Enter your choice (1-4): ")

       if choice == '1':
        show_balance(balance)
       elif choice == '2':
        balance += deposit()
       elif choice == '3':
        balance -= withdraw(balance)
       elif choice == '4':
        print("Thank you for using the Banking Program. Goodbye!")
        is_logged_in = False
       else:
        print("Invalid choice. Please try again.")

    print("Thank you! Have a nice day!")

if __name__ == "__main__":
    main()   