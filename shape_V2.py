"""
Author: Stockton Nelson
Cowitter: Troy Justesen


"""
import math

def compute_area_square(side):
    return side**2

def compute_area_rectangle(width, length):
    return width * length

def compute_area_circle(radius):
    return (radius**2)*math.pi

def compute_area(shape, one_input, two_inputs=0):
    area = 0
    if shape == 'square':
        area = compute_area_square(one_input)
    elif shape == 'circle':
        area = compute_area_circle(one_input)
    elif shape == 'rectangle':
        area = compute_area_rectangle(one_input, two_inputs)
    return area

user_input = ''
while True:
    user_input = input("What shape do you want to do(square, rectangle, circle, or quit to leave): ")
    user_input = user_input.lower()

    if user_input == 'square':
        side = float(input('What is the side length?: '))
        area = compute_area(user_input, side)
        print(f'The area is: {area:.2f}')

    elif user_input == 'rectangle':
        width = float(input('What is the width?: '))
        length = float(input('What is the length?: '))
        area = compute_area(user_input, width, length)
        print(f'The area is: {area:.2f}')

    elif user_input == 'circle':
        radius = float(input('What is the radius?: '))
        area = compute_area(user_input, radius)
        print(f'The area is: {area:.2f}')
        
    elif user_input == 'quit':
        break
