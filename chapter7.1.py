# program7_2.py
# Kylor Love 2412119
# pseudocode
# Import random
# Create empty list named numbers_random
# Use for loop to generate random munbers in range(12)
# Use numbers_random.append to add random numbers to end of list
# Sort random integers so they are in order
# Display three largest numbers using a list slice
# Display three lowest numbers using a list slice
# Display integers sorted highest to lowest
# Reverse list so it will be in descending order
# Display list highest to lowest
# Call show_list(numbers_random) function with its argument numbers_random
# Display total
# Define show_list function
# Variable named total to act as accumulator
# Add numbers in list to total
# Return total
# Collaboration statement
# Call main function

# Import random numbers to list
import random

def main():
    # Create empty list
    numbers_random = []

    # For loop to generate random numbers
    for index in range(12):
    # Use numbers_random.append to add numbers to end of list
        numbers_random.append(random.randint(0,50))
    # Sort random integers so they are in order
    numbers_random.sort()
    # Display three largest numbers using a slice
    print('\nThe three largest integers are',numbers_random[9:])
    # Display three lowest numbers using a slice
    print('The three lowest integers are', numbers_random[:3])
    # Display integers sorted highest to lowest
    print('Here are all of the integers, sorted highest to lowest...')
    # Reverse list so it will be in descending order
    numbers_random.reverse()
    # Dispaly list highest to lowest
    for numbers in numbers_random:
        print(numbers,end=' ')
    print()
    # Call show_list(numbers_random) function with its argument numbers_random
    show_list(numbers_random)
    for total in numbers_random:
        # Display total
        print('The sum of all the integers in the list is',show_list(numbers_random))
        break

# Define show_list function
def show_list(numbers_random):

    
    total = 0
    # Add numbers to total
    for numbers in numbers_random:
        total += numbers
    # Return total
    return total

    # Collaborators: None.

# Call main function
main()

    
    
