"""
Main author: Stockton Nelson
Cowitters: Jackson Kelley, Troy Justesen, Christopher Savage
"""

user_grade = float(input('What grade did you get this coures? '))

if(user_grade >= 90):
    letter = 'A'
elif (user_grade >= 80):
    letter = 'B'
elif (user_grade >= 70):
    letter = 'C'
elif (user_grade >= 60):
    letter = 'D'
elif (user_grade < 60):
    letter = 'F'

last_digit = int(user_grade) % 10
if last_digit >= 7:
    sign = '+'
elif last_digit < 3:
    sign = '-'
else:
    sign = ''
if letter == 'F':
    sign = ''
if user_grade > 95:
    sign = ''
final_grade = f"{letter}{sign}"
if(user_grade > 60):
    print(f'You pass the course with a grade of {final_grade}! YIPEEEEE!')
else:
    print(f'You did not pass the course because you got a grade of {final_grade}. :( ')