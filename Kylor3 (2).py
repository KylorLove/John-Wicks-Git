# Program3_2.py
# Kylor Love 2412119
# Prompt user for price of car as an integer.
# Prompt user for type of car new or used.
# Prompt user for price of second car. Prompt user for type of
# second car new or used. Define new as $1500 pay and used as
# 5% of total price. Compute total cost of both cars by adding
# variables from user price inputs Price and Price1.
# Display total cost of cars in currency format. Compute total
# commission pay by multiplying Price by 0.05 if car is used or adding
# $1500 if car is new then add the two values.
# Display total commission pay as 'your pay total is $' using sep='' and ,.2f fo
# to maintain currency format.

def main():
    # Prompt for price of car
    Price = int(input('Cost of car in whole numbers:'))
    # Prompt for type of first car
    new = 1500.00
    used = Price * 0.05
    Car = input('Is this car new or used?:')
    if Car == new:
        (1500)
    else:
        if Car == used:
            (Price * 0.05)
    # Prompt for price of second car
    Price1 = int(input('Cost of car in whole numbers:'))
    # Prompt for type of second car
    Car1 = input('Is this car new or used?:')
    if new:
        (1500)
    else:
        if used:
            (Price1 * 0.05)

    # Define pay based on new or used car
    print('Your pay is $',format(Car + Car1),sep='')

    # Compute sales commission total
    print('Total cost of cars is $',format(Price + Price1,',.2f'),sep='')

    # Collaborators: none.

main()

    
    
