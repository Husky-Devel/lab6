from os import system, name
from time import sleep

resultgl = 0
oprationgl = 0

def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')


def again():
    global resultgl
    global oprationgl

    if oprationgl == 1: 
     print("The lenth of your rectangle is: ", resultgl)
    elif oprationgl == 2:
     print("the width of your rectangle is: ", resultgl)
    elif oprationgl == 3:
     print("the voulum of your cube is: ", resultgl)

    print
    calc_again = input('''
    Do you want to perform another opration?
    Please type Y for Yes or N for No.
    ''')
    goodbey = 'Thank you for useing my app (the app will now exit)'
    if calc_again == 'Y':
        clear()
        main()
    elif calc_again == 'N':
        print(goodbey)
    
    else:
        clear()
        again()

def main():
    global resultgl
    global oprationgl
    
    opration = int(input('''
    Please type in the oparation you would like to complete:
    1 for length of a rectangle
    2 for width a rectangle
    3 for voulme of a cube 
    
    '''))
    
    if opration == 1:
        number1 = int(input('Enter the width of your rectangle: '))
        number2 = int(input('Enter the Perimeter of your rectangle: '))
    elif opration == 2:
        number1 = int(input('Enter the length of your rectangle: '))
        number2 = int(input('Enter the area of your rectangle: '))
    elif opration == 3:
        number1 = int(input("Enter the edge length of your cube:"))
    
    if opration == 1:
     resultgl = (number2 / 2 - number1)
     print("The lenth of your rectangle is: ", resultgl)
    elif opration == 2:
     resultgl = (number2 /  number1)
     print("the width of your rectangle is: ", resultgl)
    elif opration == 3:
     resultgl = (number1 * number1 * number1)
     print("the voulum of your cube is: ", resultgl)

    oprationgl = opration
    
    clear()
    sleep(1)
    again()
     

main()
