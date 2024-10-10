def rectangle_area(width, height):
    '''Calculates the area of a rectangle'''
    return width*height


def triangle_area(base, height):
    '''Calculates the area of a triangle'''
    return 1/2*base*height


def circle_area(radius):
    '''Calculates the area of a circle'''
    PI = 3.14
    return PI*(radius**2)


if __name__ == "__main__":
    choice = input('Press "1" to calculate the area of a rectangle.\n'
                   'Press "2" to calculate the area of a triangle.\n'
                   'Press "3" to calculate the area of a circle.\n'
                   'Please make your choice: ')
    if choice == '1':
        width = int(input('Enter a width: '))
        height = int(input('Enter a height: '))
        print(f'The area of a rectangle is {rectangle_area(width, height)}')
    elif choice == '2':
        base = int(input('Enter a base: '))
        height = int(input('Enter a height: '))
        print(f'The area of a triangle is {triangle_area(base, height)}')
    elif choice == '3':
        radius = int(input('Enter a radius: '))
        print(f'The area of a circle is {circle_area(radius)}')
