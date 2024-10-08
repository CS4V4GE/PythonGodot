def main():
    numbers = []
    print("Enter a list of numbers, type 0 when finished.")
    
    while True:
        num = float(input("Enter number: "))
        if num == 0:
            break
        numbers.append(num)
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average is: {average:.3f}")
    else:
        print("No numbers entered.")
        
main()