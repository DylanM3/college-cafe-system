from helpers import *

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def print_menu(menu):
    print() # Formatting

    for index, item in enumerate(menu, start=1):
        print(f"{index}: {item} - ${menu[item]}")

    print() # Formatting

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def get_customer_choice(menu, customer_name):

    correctChoice = False
    while correctChoice == False:

        print_menu(menu)
        customer_choice = input("What would you like to order? ")

        match customer_choice:

            case '1':
                customer_choice = "Latte"
                confirmation = confirm_customer_choice(customer_name, customer_choice)
                if confirmation == True:
                    amount = order_bulk(customer_name, customer_choice)
                    print(f"Ordering a Latte... (x{amount})")
                    return customer_choice, amount
                else:
                    clear_screen()
                    pass

            case '2':
                customer_choice = "Tea"
                confirmation = confirm_customer_choice(customer_name, customer_choice)
                if confirmation == True:
                    amount = order_bulk(customer_name, customer_choice)
                    print(f"Ordering a Tea... (x{amount})")
                    return customer_choice, amount
                else:
                    clear_screen()
                    get_customer_choice(menu, customer_name)

            case '3':
                customer_choice = "Hot Chocolate"
                confirmation = confirm_customer_choice(customer_name, customer_choice)
                if confirmation == True:
                    amount = order_bulk(customer_name, customer_choice)
                    print(f"Ordering Hot Chocolate... (x{amount})")
                    return customer_choice, amount
                else:
                    clear_screen()
                    pass

            case '4':
                customer_choice = "Cookie"
                confirmation = confirm_customer_choice(customer_name, customer_choice)
                if confirmation == True:
                    amount = order_bulk(customer_name, customer_choice)
                    print(f"Ordering a Cookie... (x{amount})")
                    return customer_choice, amount
                else:
                    clear_screen()
                    pass

            case '5':
                customer_choice = "Soft Drink"
                confirmation = confirm_customer_choice(customer_name, customer_choice)
                if confirmation == True:
                    amount = order_bulk(customer_name, customer_choice)
                    print(f"Ordering a Soft Drink... (x{amount})")
                    return customer_choice, amount
                else:
                    clear_screen()
                    pass

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

def order_bulk(customer_name, customer_choice):
    amount = int(input(f"{customer_name}, how many {customer_choice}'s do you wish to order? "))
    return amount
