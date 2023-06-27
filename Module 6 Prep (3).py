# filemaker.py
# Kylor Love 2412119
# Pseudocode
# Begin with def main():
# Open a file for writing
# Get data for each friend and write it in file
# Create while loop to gather input
# Get data for each friend
# Create if statement == to '' to break the loop once nothing is entered
# Write in files
# Display blank line
# Close the file using names_file.colse
# End program by calling the main function

def main():
    # Open a file for writing
    names_file = open('friends.txt', 'w')

    # Counter
    count = 0

    name = 'Placeholder'
    # Get data for each friend and write in file
    while names_file != '':
        # Get data for friend
        name = input('Enter first name of friend or ENTER to quit: ')

        # Add to counter
        count += 1
        
        # If statement to break loop
        if name == '': 
            break;
        age = input('Enter name (integer) of this friend: ')

        # Write in files
        names_file.write(name + '\n')
        names_file.write(age + '\n')

        # Display blank line
        print()

        # Close the file
    names_file.close()
    print('A file was created.')

    # Collaborators: none.

# Call main function
main()
