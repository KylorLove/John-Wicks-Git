### Program4_2.py
### Kylor Love 2412119
# Write def main():
# Define variables to control the loop use commission to count pay and use total_sales to count price of cars
# Use keep_going to control loop and set = to 'yes' so user can repeat the loop
# Start while loop and get input from user car = type of car new/used
# price = float(input( price of car ))
# Set if statements car == 'used' for comission += price * 0.05
# Second if statement car == 'new' for commission += 1500
# Add price of car to total_sales += price
# Prompt user to repeat the loop
# Display total_sales in currency format
# Display commission in currency format
# End with main()


def main():

    # Variables to control the loop
    commission = 0
    total_sales = 0
    keep_going = 'yes'

    # Get input from user for type of car and price
    while keep_going == 'yes':
            car = input('Is this car new or used? ')
            price = float(input('What is the sale price of car? '))
            if car == 'used':
                commission += price * .05
                total_sales += price
            if car == 'new':
                commission += 1500
                total_sales += price
    # Ask the user if thet want to repeat the loop
            keep_going = input('Do you want to calculate another car commission(Enter yes for another): ')
    # Display total_sales and commission in currency format ',.2f' and sep=''    
    print('Your total sales are $',format(total_sales,',.2f'),sep='')
    print('Your total pay is $',format(commission,',.2f'),sep='')

    

            

            
                

    
        

main()
        
    
