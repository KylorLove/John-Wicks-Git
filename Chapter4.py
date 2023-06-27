### Program4_1.py
### kylor Love 2412119
  # Start with def main():
  # Set variables for counters total_even = 0 and total_odd = 0
  # Create for loop using range function to count down from 300 to 1(300,0,-1)
  # Use if statement %23 to find multiples of 23
  # Use if statement %2 to find even multiples
  # Add even multiples to counter total_even
  # Add odd multiples to counter total_odd
  # Display numbers 300 to 1 in same line
  # Display even and odd multiples in seperate lines with '5d' character spacing
  # End with main()

def main():
    # Variables for counters
    total_even = 0
    total_odd = 0

    # For loop and range counting down
    for numbers in range(300,0,-1):
    # %23 to find multiples of 23
        if numbers %23 == 0:
    # %2 to find even multiples
            if numbers %2 == 0:
    # Adding even multiples to counter
                total_even += 1
            else:
    # Adding odd multiples to counter
                total_odd += 1
    # Display numbers from 300 down to 1 with format '5d' character spacing in a line end=''
            print(format(numbers,'5d'),end='')
    # Display totals for even and odd counters using format and '5d' charcter spacing
            print(format(total_even,'5d'),format(total_odd,'5d'))

main()
