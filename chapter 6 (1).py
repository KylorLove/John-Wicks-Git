# program6_1.py
# Kylor Love 2412119
# Psedocode
# Begin with def main():
# Open a file for writing
# Get data for each item and write it in file
# Create while loop to gather input
# Get data for each item
# Create if statement == to '' to break the loop once nothing is entered
# Display 'A record has been written to file'
# Write in files
# Display blank line to make easier to read
# Close the file using items_file.colse
# End program by calling the main function

def main():
    # Open a file for writing
    items_file = open('inventory.txt', 'w')

    name = 'Placeholder'
    # Get data for each item and write in file
    while items_file != '':
        # Get data for an item
        name = input('Enter name of inventory item or press ENTER to quit: ')
        # If statement to break loop
        if name == '': 
            break;
        price = input('Enter price of item: ')
        qty = input('Enter quantity of item: ')
        # Display record written to file
        print('A record has been written to file')

        # Write in files
        items_file.write(name + '\n')
        items_file.write(price + '\n')
        items_file.write(qty + '\n')

        # Display blank line
        print()

        # Close the file
    items_file.close()
    print('The file was created successfully and closed')

    # Collaborators: None.

# Call main function
main()
        
