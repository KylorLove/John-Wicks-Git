def main():
    # local variable named "value" in main() assigned the value 100
    value = 100
    # statement displays "The value is 100"
    print('The value is', value)
    # value variable passed as argument to change_me funtion
    change_me(value)
    print('back in main the value is',value)
    # define function change_me
def change_me(argument):
    print('I am changing the value')
    argument = 22
    print('Now the value is', argument)
main()
