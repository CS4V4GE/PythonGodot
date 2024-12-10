"""
ONLY Author: Stockton Nelson


"""
import math

def compute_area_square(side):
    area = side**2
    return area

def compute_area_rectangle(width, hight):
    area = width * hight
    return area

def compute_area_circle(raduis):
    area = float((raduis**2)*math.pi)
    return area

while True:
    user_input = input("What shape do you want to do(square, rectangle, circle, or quit to leave): ")

    if user_input == 'square':
        side = float(input('What is length of side?: '))
        print(compute_area_square(side=side))

    elif user_input == 'rectangle':
        width = float(input('What is length of width?: '))
        hight = float(input('What is length of hight?: '))
        print(compute_area_rectangle(width=width, hight=hight))

    elif user_input == 'circle':
        raduis = float(input('What is length of raduis?: '))
        print(compute_area_circle(raduis=raduis))
        
    elif user_input == 'quit':
        break