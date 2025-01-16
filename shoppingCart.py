#Christopher Savage
def display_menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
# adds item and pricing to the shopping cart
def add_item(names, prices):
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? "))
    names.append(item)
    prices.append(price)
    print(f"'{item}' has been added to the cart.")
# shows items in the cart and the prices.
def view_cart(names, prices):
    print("\nThe contents of the shopping cart are:")
    print("-"*30)
    if len(names) == 0:
        print("The cart is empty.")
    else:
        for i in range(len(names)):
            print(f"{i + 1}. {names[i]} - ${prices[i]:.2f}")
    print("-"*30)
#asks what item to remove
def remove_item(names, prices):
    if len(names) == 0:
        print("The cart is empty.")
        return

    view_cart(names, prices)
    choice = int(input("Which item would you like to remove? "))
    print("-"*30)
    if 1 <= choice <= len(names):
        index = choice - 1  
        removed_item = names[index]
        names.pop(index)
        prices.pop(index)
        print(f"{removed_item} was removed from the cart.")
    else:
        print("Sorry, that is not a valid item number.")
        return
    print("-"*30) 
#get total price of cart
def compute_total(prices):
    total = sum(prices)
    print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")
    print("_"*30)
#Main program functions
def main():
    print("Welcome to your shopping cart.")

    names = []
    prices = []
    
    while True:
        display_menu()
        choice = input("Please enter an action: ")
        
        if choice == "1":
            add_item(names, prices)
        
        elif choice == "2":
            view_cart(names, prices)
        
        elif choice == "3":
            remove_item(names, prices)
        
        elif choice == "4":
            compute_total(prices)
        
        elif choice == "5":
            print("Thank you for shopping with [COMPANY]. Come again soon!")
            break
        
        else:
            print("Invalid input. Pleases select 1-5")

# Start the program
if __name__ == "__main__":
    main()