# filemaker.py
# Kylor Love 2412119
# Pseudocode
# Begin with def main():
# Open .txt file
# Set counter variable to 0
# Read first line from file using names_file.readline
# If field was reaad continue proccessing
# Read age field
# Strip the newlines from the fields using .rstrip
# Define counter as += 1
# Define average as age/counter 
# Display the record in single line
# Display blank line
# Display average age
# Close the file names_file.close()
# End program by calling the main function

def main():
    # Open text file
    names_file = open('friends.txt', 'r')

    # Set counter variable to 0
    counter = 0
    # Read first line from file
    name = names_file.readline()

    # If field was read continue proccessing
    while name != '':

        # Read age field
        age = names_file.readline()
 
        # Strip the newlines from the fields
        name = name.rstrip('\n')

        age = int(age.rstrip('\n'))

        # Define counter
        counter +=1

        # Define average variable
        average = age/counter

        # Display the record
        print('My friend',name,'is',age,'years old.',end='')

        # Display blank line
        print()
        
        # Read name field of next record
        name = names_file.readline()
        
    print('Average age of friends is',average)
    # Close the file
    names_file.close()

    # Collaborators: none.

# Call main function
main()
