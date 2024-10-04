print("Please enter the following information:")

# This prints a blank line
print()

first = input("Please enter your First name: ")
last = input("Please enter your Last name: ")
email = input("Please enter your Email address: ")
phone = input("Please enter your Phone number: ")
job_title = input("Please enter your Job title: ")
id_number = input("Please enter your ID Number: ")

# This time I used a \n to make a blank line before this:
print("\nThe ID Card is:")
print("-" * 40)
print(f"{last.upper()}, {first.upper()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print("-" *40)

