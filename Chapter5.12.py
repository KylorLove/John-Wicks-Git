### Program5_2.py
### Kylor Love 2412119
### pseudocode
  # import math to use it's functions if needed
  # define main function
  # set variables to gather user input named accordingly
  # set variables for calculations named accordinly
  # display paint needed with no decimal places
  # display price of paint in currency format
  # collaboration statement
  # call main
# import math module to use it's functions if needed
import math
# Define main function
def main():
    # Set variables to gather user input named accordingly
    length = int(input('Enter length of the room '))
    height = int(input('Enter height of the room '))
    width = int(input('Enter width of the room '))
    price = float(input('Enter price of a can of paint '))
    covers = int(input('Enter square feet covered by one can of paint '))

    # Set variables for calculations named accordingly
    room_size = length * width * height
    paint_needed = room_size/covers

    total = paint_needed * price
    # Display cans of paint needed without decimals
    print('This job requires',format(paint_needed,'.0f'),'cans of paint')
    # Dispaly price of paint in currency format
    print('Total price of paint for this job is $',format(total,',.2f'),sep='')

   # Collaborators: None.
# Call main    
main()
