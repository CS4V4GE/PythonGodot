number = int(input("Please enter a positive number:  "))
while number < 0:
    print("That is not a positive number.")
    number = int(input("Please enter a positive number:  "))
print(f"The number is {number}")

