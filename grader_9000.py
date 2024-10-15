"""
Main author: Stockton Nelson
Cowitters: [enter name here]
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

if(letter == 'A' or 'B' or 'C'):
    print(f'You pass the course with a grade of {letter}! YEPPY!')
else:
    print(f'You did not pass the cource because you got a grade of {letter}. :( ')