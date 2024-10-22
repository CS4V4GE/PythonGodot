# Christopher Savage
priceChild = float(input("What is the price of a childs meal?   "))
priceAdult = float(input("What is the price of an adult meal   "))
quantityChilderen = int(input("How many kids are there?  "))
quantityAdults = int(input("How many adults are there?  "))
taxRate = float(input("What is the tax rate %?   "))

# Math
subtotal = (priceChild * quantityChilderen + priceAdult * quantityAdults)
tip15 = (subtotal * 0.15)
tip20 = (subtotal * 0.20)
tip25 = (subtotal * 0.25)
print("Tip Percentage:")
print(f"15%: ${tip15:.2f}| 20%: ${tip20:.2f}| 25%: ${tip25:.2f}")
tip = float(input("What tip ($ amount) are you leaving?   "))
salesTax = (subtotal * (taxRate/100))
total = (subtotal + salesTax + tip)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax:  ${salesTax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
# Payment

money = float(input("Money Given: $"))
change = (money - total)
print(f"Your change is ${change:.2f}")
print("Thank you for your patronage!")
print("Have a good day!")
print("_"*30)