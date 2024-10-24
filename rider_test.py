
"""
Main Author: Stockton Nelson
CoWitters: Christopher Savage,

file: 
"""

"""
Basic rules:

1. No one under 36 inches may ever ride, either by themselves or with another rider.

2. Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

3. If there are two riders and one of them is at least 18 years old, they may ride together.

Strech Rules:

1.If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.

2.If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)

3.If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)
"""

first_rider_age = int(input("What is the age of the first rider? "))
first_rider_hight = int(input("What is the height of the first rider? "))
fastpass = input("Does the rider have a fast pass? (Yes/No)? ").lower()
extra_rider = input("Is there a second rider (yes/no)? ").lower()
#we only need to check yes becaseu why check no?
if extra_rider == 'yes':
    second_rider_age = int(input("What is the age of the first rider? "))
    second_rider_hight = int(input("What is the height of the first rider? "))


#rider checker
if extra_rider == 'yes':

    if (((first_rider_age or second_rider_age >= 18) or ((first_rider_age and second_rider_age >= 12) or fastpass == 'yes') or (((first_rider_age >= 16 or second_rider_age >= 16) and (first_rider_age >= 14 or second_rider_age >= 14))) and (first_rider_hight or second_rider_hight >= 62) and (first_rider_hight and second_rider_hight >=  36))):
        can_ride = True

    else: 
        can_ride = False

else:
    if ((first_rider_age >= 18) or (first_rider_age >= 12 and fastpass == 'yes' )) and first_rider_hight >= 62:
        can_ride = True

    else: 
        can_ride = False

if can_ride == True:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")