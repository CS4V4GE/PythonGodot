
"""
Stockton Nelson, Troy Justesen

file. Multiple_Lists.py
"""
account_name_list = []
balance_list = []

print('Enter the names and balances of bank accounts (type: quit when done)')
while True:
    account_name = input('What is the name of this account?')

    if account_name == 'quit':
        break

    balance = float(input('What is the balance? '))

    account_name_list.append(account_name)
    balance_list.append(balance)

#display account name with the balance
print('Account Information: ')
for number in range(len(account_name_list)):
    account = account_name_list[number]
    balance = balance_list[number]
    print(f'{account} - {balance:.2f}')

#find total and average here 
total = 0
for balance in balance_list:
    total += balance
average = total / len(balance_list)

print(f'Total: {total:.2f}')
print(f'Average: {average:.2f}')
