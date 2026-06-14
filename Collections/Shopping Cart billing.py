#SHOPPING CART PROGRAM!!
##This program allows users to add items to a shopping cart, view the cart, and calculate the total cost.
### Fundamental concepts used: Lists, Functions, Loops, Conditionals

foods = []  # Initialize an empty list to store food items
prices = []  # Initialize an empty list to store prices of the food items
total= 0  # Initialize total cost to 0

while True:
    food = input("Enter the name of the food item to purchase (Press q to quit): ")
    if food.lower() == 'q':
        break  # Exit the loop if the user enters 'q'
    else:
        price = float(input(f"Enter the price of {food}: $")) # Get the price of the food item from the user

    
    foods.append(food)  # Add the food item to the list
    prices.append(price)  # Add the price to the list

print("\n--------YOUR SHOPPING CART--------")
 
for food in foods:
    print(food, end = ",")    # Print each food item in the shopping cart with a space in between food and price

for price in prices:
       total += price  # Calculate the total cost by adding each price to the total variable

print(f"\n Your Total cost: ${total:.2f}")  # Print the total cost formatted to 2 decimal places       