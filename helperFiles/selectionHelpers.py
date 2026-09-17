from helpers import *

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# PRINT MENU (ENUMERATE SELECTION NUMBERS)
def print_menu(menu):
    print() # Formatting

    for index, item in enumerate(menu, start=1):
        print(f"{index}: {item} - ${menu[item]}")

    print() # Formatting

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def get_customer_choice(menu, customer_name):
    print_menu(menu)
    customer_choice = input("What would you like to order? ")

    match customer_choice:

        case '1':
            customer_choice = "Latte"
            confirmation = confirm_customer_choice(customer_name, customer_choice)
            if confirmation == True:
                print("Ordering a Latte...")
                return customer_choice
            else:
                clear_screen()
                get_customer_choice(menu, customer_name)

        case '2':
            customer_choice = "Tea"
            confirmation = confirm_customer_choice(customer_name, customer_choice)
            if confirmation == True:
                print("Ordering a Tea...")
                return customer_choice
            else:
                clear_screen()
                get_customer_choice(menu, customer_name)

        case '3':
            customer_choice = "Hot Chocolate"
            confirmation = confirm_customer_choice(customer_name, customer_choice)
            if confirmation == True:
                print("Ordering a Hot Chocolate...")
                return customer_choice
            else:
                get_customer_choice(menu, customer_name)

        case '4':
            customer_choice = "Cookie"
            confirmation = confirm_customer_choice(customer_name, customer_choice)
            if confirmation == True:
                print("Ordering a Cookie...")
                return customer_choice
            else:
                get_customer_choice(menu, customer_name)

        case '5':
            customer_choice = "Soft Drink"
            confirmation = confirm_customer_choice(customer_name, customer_choice)
            if confirmation == True:
                print("Ordering a Soft Drink...")
                return customer_choice
            else:
                get_customer_choice(menu, customer_name)

        case _:
            print("Error: Item Not Found.")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def confirm_customer_choice(customer_name, customer_choice):
    confirmation = input(f"{customer_name}, you selected {customer_choice}. Is this correct? (y/n) ")
    if confirmation.lower() in ['yes', 'y', 'correct']:
        return True
    else:
        return False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=