### Program5_3.py
### Kylor Love 2412119
### pseudocode
  # import random module
  # set variables for constants
  # set counter variable to control loop
  # create a while loop
  # display shot hit or missed using if/elif statements
  # call main
   # Import random module
import random
   # Constants
TRUE = 1
FALSE = 0
def main():
    # Counter to control loop
    ammo = 10
    health = 5
    # While loop
    while health <= 5:
    # Display shot hit or missed using if/elif statements
        if random.randint(FALSE,TRUE)==TRUE:
            print('Shot fired! Enemy was hit!')
            health -= 1
        elif health == 0:
            print('You Won!')
            break
        elif ammo == 0:
            print('GAME OVER')
            break   
        else:
            print('Shot fired! Enemy missed.')
            ammo -= 1
        
            
    # Call main function
main()
