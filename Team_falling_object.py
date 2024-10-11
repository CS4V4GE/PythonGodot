"""
add names
Authors: Stockton Nelson, Troy Justesen, Jakcson Kelley, Christopher Savage

files: sn_falling_object.py
"""
import math

print("Welcome to the velocity calculator. Please enter the following:\n")

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#this is all the math in the whole code. V_terminal is the challenge part
c = (1 / 2) * p * A * C
velocity = math.sqrt((m*g)/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))
earth_velocity = math.sqrt((m*9.8)/c) * (1 - math.exp((-math.sqrt(m*9.8*c)/m)*t))
jupiter_velocity = math.sqrt((m*24)/c) * (1 - math.exp((-math.sqrt(m*24*c)/m)*t))

#according to google search it said that cross-sectional area of flat is 0.45 and head first is 0.18.
#that is how i found this number if you ask me.
flat_skydiver = math.sqrt((m*g)/0.45) * (1 - math.exp((-math.sqrt(m*g*0.45)/m)*t))
head_first_skydiver = math.sqrt((m*g)/0.18) * (1 - math.exp((-math.sqrt(m*g*0.18)/m)*t))

#this is the prints
print(f"\nThe inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {velocity:.3f} m/s")
print(f"Velocity and {t} seconds with earth gavity: {earth_velocity:.3f} m/s")
print(f"Velocity and {t} seconds with earth gavity: {jupiter_velocity:.3f} m/s")
print(f"Velocity and {t} seconds of falt skydiver: {flat_skydiver:.3f} m/s")
print(f"Velocity and {t} seconds with headfirst skydiver: {head_first_skydiver:.3f} m/s")

user_input = input("\nWhat termianal velocity do you want to see? (flat or head)")
if (user_input == "flat"):
    v_terminal = math.sqrt((m*g)/0.45)
    print(f"The terminal velocity of flat skydiver is: {v_terminal:.3f}")
elif (user_input == "head"):
    v_terminal = math.sqrt((m*g)/0.18)
    print(f"The terminal velocity of flat skydiver is: {v_terminal:.3f}")
else:
    print("miss input")