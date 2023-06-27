# Assignment 3 Prep
# Kylor Love 2412119
# Set guidelines for the quantities of coffee and their prices.
# prompt the user for input pounds of coffee.
# Define the sales tax and the cost of shipping.
# Compute the total cost by multiplying quantity, price, sales tax and add shipping.
# Define total before tax as Subtotal by mulyiplying Input amount from user by price
# assigned to specific quantity.
# subtract shipping cost if subtotal is greater than or equal to $150.
# Present Cost breakdown of coffee, shipping, tax, and total combined.

# Quantity of coffee

Qty1 = 40
Qty2 = 20
Qty3 = 10

# Prices of coffee

Price1 = 7.5
Price2 = 8.75
Price3 = 10
Price4 = 12

# Get the amount of coffe to be ordered

Amount = int(input('Enter pounds of coffee:'))

# total before tax

sub1 = (Amount * Price1)
sub2 = (Amount * Price2)
sub3 = (Amount * Price3)
sub4 = (Amount * Price4)

# Sales tax

tax = 0.07

# Shipping cost

shipping = (Amount * 1)

# Determine price of coffee based on quantity

if Amount >= Qty1:
    print('Total','$',format(Amount * Price1 + Amount * Price1 * tax + shipping,'.2f'))
    print('7% sales tax','$',format(Amount * Price1 * tax,',.2f'))
    print('Shipping cost','$',format(shipping,',.2f'))
    print('Cost of coffee','$',format(sub1,',.2f'))
else:
    if Amount >= Qty2:
        print('Total','$',format(Amount * Price2 + Amount * Price2 * tax + shipping,',.2f'))
        print('7% sales tax','$',format(Amount * Price2 * tax,',.2f'))
        print('Shipping cost','$',format(shipping,',.2f'))
        print('Cost of coffee','$',format(sub2,',.2f'))
    else:
        if Amount >= Qty3:
            print('Total','$',format(Amount * Price3 + Amount * Price3 * tax + shipping,',.2f'))
            print('7% sales tax','$',format(Amount * Price3 * tax,',.2f'))
            print('Shipping cost','$',format(shipping,',.2f'))
            print('Cost of coffee','$',format(sub3,',.2f'))
        else:
            if Amount <= Qty3:
                print('Total','$',format(Amount * Price4 + Amount * Price4 * tax + shipping,',.2f'))
                print('7% sales tax','$',format(Amount * Price4 * tax,',.2f'))
                print('Shipping cost','$',format(shipping,',.2f'))
                print('Cost of coffee','$',format(sub4,',.2f'))

# Collaborators: none
                            
        
           
            
        





   
