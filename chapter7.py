# program7_1.py
# Kylor Love 2412119
# pseudocode
# Create an empty list named list_friends
# Set counter for how many friends
# Variable to assign friends names called friends_names
# Create while loop to add friends to the list
# Use append method to add friend to end of the list
# Display number of friends entered
# Display text
# Add friend to start of list
# Dispaly text
# Create for loop to display friends names add +1 to toal for added friend
# Delete a friend using del
# Sort friends names in list
# for loop to display revised list of friends in alphabetical order
# Collaboration statement
# Call main function

def main():
    
    # Empty list
    list_friends = []

    # Counter for how many friends
    total = 0

    # Variable to assign friends names
    friends_names = input('Enter the first name of a friend of ENTER to quit ')
    
    # While loop to add friends to the list
    while friends_names != '':

        # Append method to add friends to end of list
        list_friends.append(friends_names)
        friends_names = input('Enter the first name of a friend of ENTER to quit ')
        total += 1

    # Display number of friends entered
    print('You made a list of',total,'friends.')
        
    # Display text    
    print('OOPS, you forgot to enter a very good friend.')
    print('If she is not in the list, she will be added now at the start of the list.')
    print()
    
    # Add friend to start of list
    list_friends.insert(0,'Jenny')

    # Display text
    print('Here are my friends...')

    # Create for loop to dispaly friends names +1 to total for added friend
    for names in range(total + 1):
        print(list_friends[names],end=' ')
    print()
    print()
          
    print('Sadly, one friend moved away and was deleted.')
    print('Here are my remaining friends in alphabetical order')

    # Delete a friend
    del list_friends[2]

    # Sort friends list
    list_friends.sort()

    # for loop to display revised list of friends in alphabetical order
    for names in range(total):
        print(list_friends[names], end=' ')

    # Collaborators: None.
    
# Call main function
main()
        
    
    
