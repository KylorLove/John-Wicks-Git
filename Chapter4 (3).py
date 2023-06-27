### program4_3.py
### Kylor Love 2412119
  # Start with def main():
  # Create for rows loop with range function counting down from 9 to 1(9,0,-1)
  # Create a second nested for columns loop with range(rows)
  # Display end='' to keep single line
  # Display *
  # End with main()

def main():
    # Create nested loop
    for rows in range(9,0,-1):
        for columns in range(rows):
    # Display * in a stair step
            print(' ',end='')
        print('*')

main()
