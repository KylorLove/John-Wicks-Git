# program3_1.py
# Kylor Love 2412119
# Prompt for the price. Prompt for the quantity. Prompt for taxes with clear
# inputs defined yes/no. Define the tax cost.
# Define the shipping cost. Compute subtotal price * quantity. Set guidelines
# for shipping is subtotal >= $25 remove shipping cost from total. If price is
# < $25 add $6.00 shipping cost to total. Calculate total by multiplying
# subtotal and tax together then add in shipping if applicable.
# aDisplay four line outputs for Subtotal,tax,shippinf, and total. All in
# currency format.

def main():
    # Prompt for price
    Price = int(input('What is the price in whole numbers:'))
    # Prompt for quantity
    Qty = int(input('How many of this item?:'))
    #Tax cost
    Tax = 0.07
    # Prompt for tax
    Taxable = input('Does this item have taxes added? yes/no:')
    yes = Tax
    no = Tax
    if Taxable == 'yes':
        Tax = 0.07
    else:
        if Tax == no:
            Tax = 0
    # Compute subtotal
    Subtotal = Price * Qty
    # Shipping cost
    Shipping = 6.00
    # Determine shipping
    if Subtotal >= 25.00:
        Shipping = 0
    # Compute total
    Total = Price * Qty + Price * Qty * Tax + Shipping
    # Diplay outputs in currency form
    print('Your subtotal is $',format(Subtotal,',.2f'),sep='')
    print('Your tax is $',format(Tax * Subtotal,',.2f'),sep='')
    print('Your shipping is $',format(Shipping,',.2f'),sep='')
    print('Your total is $',format(Total,',.2f'),sep='')

    # Collaborators: none.

main()

        
