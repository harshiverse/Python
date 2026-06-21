# Python Slot Machine Game
#In this game, the player starts with a certain amount of money and can choose to play the slot machine. 
#Each play costs a certain amount, and the player can win different amounts based on the outcome of the slot machine.

import random

def spin_row():
    symbols = ["🐻", "🦇", "🦋", "🐼", "🐰"]

    return [random.choice(symbols) for _ in range(3)]
  
def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        print("Jackpot! You won 10 times your bet!")
        return bet * 10
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print("You won 2 times your bet!")
        return bet * 2
    else:
        print("No win. Better luck next time!")
        return 0

def main():
    balance = 100  # Starting balance

    print("-------------------------------")
    print("Welcome to the Slot Machine Game!")
    print("Symbols: 🐻🦇🦋🐼🐰") #Use windows + ; keys together to open the emoji bar
    print("-------------------------------")

    while balance > 0:
        print(f"Current Balance: ${balance: .2f}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Invalid input. Please enter a valid bet amount.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient balance!!")
            continue

        if bet <=0:
            print("Place a higher bid. Bet must be greater than 0.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout: .2f}!")
        else:
            print("Sorry!You lost your bet.")

        balance += payout 

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break
         
if __name__ == "__main__":
    main()    