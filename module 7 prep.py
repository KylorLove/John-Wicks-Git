# module 7 prep assignment
# Kylor Love 2412119
# Pseudocode
# import random
# Create empty list
# For loop to generate random numbers
# Display 4th element in the list numbers_random
# Display element at 9th index in list numbers_random
# Display smallest element in the list numbers_random using min function
# Call change_list function and catch return array as list2
# Define cahnge_list function
# Use slicing on list
# Display size of list
# Sort new list
# for loop to display sorted random integers
# Display sorted list
# Return list
# Call main function

# Import random
import random

def main():
    # Create empty list
    numbers_random = []

    for index in range(12):
        numbers_random.append(random.randint(50, 100))
    # Dispaly list of random integers
    print('Here is a list of random numbers...')
    for numbers in numbers_random:
        print(numbers,end=' ')
    # Display 4th element in the list numbers_random
    print('\nThe fourth element in the list is', numbers_random[3])
    # Display element at index 9 in numbers_random
    print('The element at index 9 is', numbers_random[9])
    # Display smallest element in the list numbers_random usin min function
    print('The smallest element in the list is', min(numbers_random))
    # Call change_list function and catch returned array as list2
    list2 = change_list(numbers_random)
    print('Change_list returned this sorted list...')
    for numbers in list2:
        print(numbers,end=' ')

# Define change_list function
def change_list(mylist):
    # Slice list
    numbers2 = mylist[3:-3]
    # Display size of list
    print('The size of the list is now', len(numbers2))
    # Sort the new list
    numbers2.sort()
    # Return list
    return numbers2
        
# Call main function()
main()
