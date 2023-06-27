### Final Exam prep
### pseudocode

def main():
### 1
    for numbers in range(10,51,5):
        print(numbers,end=' ')
    print()
### 2
    my_info = open('aboutme.txt', 'w')

    my_info.write('Kylor Love\n')
    my_info.write(str('21' + '\n'))

    my_info.close()
    print()
### 3
    price_1 = 35799.19
    price_2 = 42539.57
    total = price_1 + price_2
    print('$',format(total,',.2f'),sep='')
    print()
### 4
    item_price = float(input('Enter price of the item: '))
    qty = int(input('Enter quantity of item in stock: '))
    value = item_price * qty
    print('total inventory value: $',format(value,',.2f'),sep='')
    print()
### 5
    small = int(input('Enter a number: '))
    large = int(input('Enter a larger number: '))
    remainder = large%small
    print('The remainder is: ',remainder)
### 6
   
### 7
    age = int(input('Enter age: '))
    if age in range(13,20):
        print(True)
### 8
    int(input('Enter an even number
    while range(1,100,2):
    int(input('Enter an even number: '))
    if range(2,100,2):
        print('Stop')
### 9
    numbers = 5
    total = 0
    for nums in range(numbers):
        integers = float(input('Enter a number as a float: '))
        total += integers
    print(total)
### 10
    
### 11
    names = open('gang.txt', 'w')
    names.write('Penny\n')
    names.write('19' + '\n')
    names.close()

    names_show = open('gang.txt', 'r')
    file_contents = names_show.read()
    names_show.close()
    print(file_contents)






### 12
    nums = [8,3,4,6,77,32,1,2,9]
    print(len(nums))
    print(max(nums))
    print(min(nums))
    print(nums[8:])
    
    
    
                       

main()
