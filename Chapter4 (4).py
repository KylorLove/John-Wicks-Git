### Program4_4.py
### Kylor Love 2412119
  # Start with def main():
  # Add variable for counter called total
  # Prompt for user input using int(input())
  # Create while loop != 0 to end loop by typing 0
  # Add numbers to counter by total += number
  # Display total
  # End with main()
  

def main():

    entered_value = int(input('Enter a small integer(or type 0 to end):'))
    total = 0
    number_counter= 0

    while entered_value != 0:
            total = total + entered_value
            number_counter = number_counter + 1
            entered_value = int(input('Enter a small integer(or type 0 to end):'))
            print(total, total/number_counter)
        


main()
