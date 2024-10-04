# Christopher Savage
priceChild = float(input("What is the price of a childs meal?   "))
priceAdult = float(input("What is the price of an adult meal   "))
quantityChilderen = int(input("How many kids are there?  "))
quantityAdults = int(input("How many adults are there?  "))
taxRate = float(input("What is the tax rate?   "))
#math
subtotal = (priceChild * quantityChilderen + priceAdult * quantityAdults)
salesTax = (subtotal * taxRate)
total = (subtotal + salesTax)
print(f"Subtotal: {subtotal}")
print(f"Sales Tax:  {salesTax}")
print(f"Total: {total}")

money = float(input("Money Given :"))
change = (money - total)
print(f"Your change is {change:.2f}")