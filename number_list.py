"""
Main Author: Stockton Nelson
cowitter: Jackson Kelley, Troy Justesen

file: number_list.py
"""

import sys

number_list = []

def number_sum():
    sum = 0
    for numbers in number_list:
        sum += numbers
    return numbers

def number_average():
    return number_sum() / len(number_list)

def largest_number():
    return number_list[len(number_list)-1]

def smallest_positive_number():
    smallest = sys.maxsize
    for numbers in number_list:
        if numbers > 0 and numbers < smallest:
            smallest = numbers
    return smallest

while True:
    
    user_input = int(input('Add a number or do 0 to finish: '))

    if user_input == 0:
        number_list.sort()
        print(f"The sum is: {number_sum()}")
        print(f"The average is: {number_average()}")
        print(f"The largest number is: {largest_number()}")
        print(f"The smallest positive number is: {smallest_positive_number()}")
        print("The sorted list is:")
        for numbers in number_list:
            print(numbers)
    
    else:
        number_list.append(user_input)
