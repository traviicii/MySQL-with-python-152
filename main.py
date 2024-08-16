from customer_add import add_customer
from customer_fetch import fetch_all_customers, fetch_customer
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def customer_menu():
    clear()
    while True:
        action = input('''
1 - Add Customer
2 - View Customer Details
3 - Display All Customers
4 - Main Menu
5 - Clear Terminal
''')
        
        if action == '1':
            add_customer()
        elif action == '2':
            fetch_customer() # view specific customer
        elif action == '3':
            fetch_all_customers() # display all customers
        elif action == '4':
            break
        elif action == '5':
            clear()



while True:

    action = input('''
1 - Customer Actions
2 - Book Actions
3 - Quit
''')
    
    if action == '1':
        customer_menu() # customer action stuff
    elif action == '2':
        pass # book action stuff
    elif action == '3':
        break
    else:
        print("Pick a number fool!")