# chapter 2 prep assignment
# Kylor Love 2412119
# pseudocode
# define main
# set variables to gather user input named accordingly
# set variables for calculations
# display average score accuarate to 2 decimal spaces
# call main

# define main function
def main():
    # set variables to gather user input named accordingly
    test1 = int(input('Enter test score for test1: '))
    test2 = int(input('Enter test score for test2: '))
    test3 = int(input('Enter test score for test3: '))
    # set variables for calculations
    total = test1 + test2 + test3

    average = total/3
    # display average score accuarate to 2 decimal spaces
    print('The average of the 3 test scores is: ',format(average,',.2f'),'%',sep='')
# call main()
main()
