"""
Main Author: Stockton Nelson
[Co-witter goes here]

file: HR_system
"""

names = []

id_numbers = []

job_titles = []

paychecks = []

with open('hr_system.txt') as file:
    
    for row in file:
        
        line = row.split()

        names.append(line[0])
        id_numbers.append(line[1])
        job_titles.append(line[2])
        
        salary = float(line[3])
        bi_week_pay = salary / 24

        bonus  = 0
        if line[2].lower() == 'engineer':
            bonus = 1000

        paychecks.append(bi_week_pay + bonus)

for index in range(len(names)):
    print(f'{names[index]} (ID: {id_numbers[index]}), {job_titles[index]} - ${paychecks[index]:.2f}')