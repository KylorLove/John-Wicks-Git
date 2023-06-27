# Chapter4_Prep
# Kylor Love 2412119

# Start with def main():
# Write in for loop and utilize range fuction.
# start at (5, end at 50, and move up in intervals of 5)
# create variable named square and **2 numbers specified in the range
# create cube variable **3 and cube numbers from the range
# display outputs in a table by using '\t' between variable names
# use print funtion to print a table with 3 colums one for each variable
# enter main()

def main():
    # for loop anf range function
    for number in range(5,51,5):
    # square variable for squaring numbers in range
        square = number**2
    # cube variable
        cube = number**3
    # display variables in colums by using tab
        print(number,'\t',square,'\t',cube)
    # end with main()
        

main()
    
    

