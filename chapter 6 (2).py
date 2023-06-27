# program6_2.py
# Kylor Love 2412119
# Pseudocode
# Begin with def main():
# Display title of program
# Set variable named value = to 0
# Open .txt file
# Read first line from file using items_file.readline
# If field was reaad continue proccessing
# Read price field
# Read quantity field
# Strip the newlines from the fields using .rstrip
# Define value
# Display the record using currency format
# Display blank line
# Display total value
# Close the file items_file.close()
# End program by calling the main function

def main():
    
    # Dispaly program title
    print('Chica Chic Inventory')
    print()

    # Set value = to 0
    value = 0
    # Open text file
    items_file = open('inventory.txt', 'r')

    # Read first line from file
    name = items_file.readline()

    # If field was read continue proccessing
    while name != '':

        # Read price field
        price = items_file.readline()

        # Read quantity field
        qty = items_file.readline()

        # Strip the newlines from the fields
        name = name.rstrip('\n')
        price = float(price.rstrip('\n'))
        qty = int(qty.rstrip('\n'))

        # Add to value
        value += price * qty

        # Display the record
        print(name + ',','$'+format(price),'each,',qty,'in stock,','value','$'+format(float(price)*int(qty),'.2f'),end='')

        # Display blank line
        print()

        # Read name field of next record
        name = items_file.readline()

    # Display total value
    print()
    print('Total value is:','$'+format(value))    

    # Close te file
    items_file.close()

    # Collaborators: None.

# Call main function
main()
    
    
