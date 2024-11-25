
"""
Stockton Nelson, Troy Justesen

file. Multiple_Lists.py
"""
account_name_list = []
balance_list = []

def find_total():
    total = 0
    for balance in balance_list:
        total += balance
    return total

def find_highest_balnce_index():
    sorted_balance_list = balance_list.copy()
    sorted_balance_list.sort()
    highest_balance = sorted_balance_list[len(sorted_balance_list)-1]
    for index in range(len(balance_list)):
        if balance_list[index] == highest_balance:
            return index

#display account name with the balance
def print_info_list():
    print('\nAccount Information: ')
    for number in range(len(account_name_list)):
        account = account_name_list[number]
        balance = balance_list[number]
        print(f'{account} - {balance:.2f}')
    print()


print('Enter the names and balances of bank accounts (type: quit when done)')
while True:
    account_name = input('What is the name of this account?')

    if account_name == 'quit':
        break

    balance = float(input('What is the balance? '))

    account_name_list.append(account_name)
    balance_list.append(balance)

print_info_list()

#find total and average here 

total = find_total()
average = total / len(balance_list)
index = find_highest_balnce_index()

print(f'\nTotal: {total:.2f}')
print(f'Average: {average:.2f}')
print(f'Highest balance: {account_name_list[index]} - {balance_list[index]:.2f}')

while True:
    user_input = input('Do you want to update an account? ').lower()

    if user_input =='no':
        break

    elif user_input == 'yes':

        user_index = int(input('What account index do you want to update? '))
        user_amount = float(input('What is the new amount? '))

        balance_list[user_index] = user_amount

        print_info_list()
    else:
        print('Try again (yes/no)')
print_info_list()