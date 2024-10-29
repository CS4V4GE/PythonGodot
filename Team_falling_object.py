"""
Author: Stockton Nelson

files: sn_falling_object.py
"""
#Team project
import math

print("Welcome to the velocity calculator. Please enter the following:\n")

m = float(input("mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))


c = (1 / 2) * p * A * C
velocity = math.sqrt((m*g)/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))
earth_velocity = math.sqrt((m*9.8)/c) * (1 - math.exp((-math.sqrt(m*9.8*c)/m)*t))
jupiter_velocity = math.sqrt((m*24)/c) * (1 - math.exp((-math.sqrt(m*24*c)/m)*t))
v_terminal = math.sqrt((m*g)/c)

print(f"\nThe inner value of c is: {c:.3f}")
print(f"The velocity after 10.0 seconds is: {velocity:.3f} m/s")
print(f"Velocity with earth gavity: {earth_velocity:.3f} m/s")
print(f"Velocity with earth gavity: {jupiter_velocity:.3f} m/s")
print(f"The terminal velocity is: {v_terminal:.3f}")

