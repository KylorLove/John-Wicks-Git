### Program5_1.py
### Kylor Love 2412119
### pseudocode
  # Import random module
  # Define main function
  # Set variables to gather user input
  # set counters for amount of even and odd numbers and total
  # For loop to display random numbers
  # number variable to gather random numbers
  # total variable += to add numbers to total
  # If/else statement with %2==0 to check for evens and odds
  # Display amount of even and odd numbers
  # Display total generations of the loop
  # Collaborators statement
  # Call main function
  
# import random module  
import random
# define main
def main():
    # set variables for user input named accordingly
    gens = int(input('How many integers are to be generated: '))
    lower = int(input('Lower limit for range is: '))
    upper = int(input('Upper limit for range is: '))
    # set counters for amount of even and odd numbers and total
    total = 0
    even = 0
    odd = 0
    # for loop to display random numbers
    for nums in range(gens):
        # numbers variable to gather random numbers in memory
        numbers = random.randint(lower,upper)
        print(numbers,end=' ')
        # add numbers to total
        total += numbers
        # if/else statements to add amount of even and odd numbers
        if (numbers % 2)==0:
             even += 1
        else:
             odd += 1
    # display total and amount of odds and evens
    print()
    print('There are',even,'evens and',odd,'odds')
    print()
    print('The total of those',gens,'random numbers is',total)


    # Collaborators: None.
# call main
main()     
        
