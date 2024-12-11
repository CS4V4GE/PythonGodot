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

def compute_area(shape, one_input, two_inputs):
    area = 0
    if shape == 'square'
        area = comput_area_square(one_input)
    elif shape == 'circle'
        compute_area_circle(one_input)
    elif shape == 'rectangle'
        compute_area_rectangle(one_input, two_inputs)
    return area

user_input = ''
while True:
    user_input = input("What shape do you want to do(square, rectangle, circle, or quit to leave): ")
    user_input = user_input.lower()

    if user_input == 'square':
        side = float(input('What is the side length?: '))
        print(compute_area(shape, side))

    elif user_input == 'rectangle':
        width = float(input('What is the width?: '))
        length = float(input('What is the length?: '))
        print(compute_area(shape, width, length))

    elif user_input == 'circle':
        radius = float(input('What is the radius?: '))
        print(compute_area(shape, radius))
        
    elif user_input == 'quit':
        break
