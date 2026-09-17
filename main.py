# IMPORTS AND INITS
import os
from helpers import *
from selectionHelpers import *

ordering = True
total_price = 0
customer_order = []

# PRICES

menu = {
    "Latte" : "3.20",
    "Tea" : "2.40",
    "Hot Chocolate" : "3.00",
    "Cookie" : "1.80",
    "Soft Drink" : "2.20"
}

# PROGRAM LOOP

customer_name = greet_customer()
while ordering:
    customer_choice = get_customer_choice(menu, customer_name)

    customer_order.append(customer_choice)
    total_price += float(menu[customer_choice])

    order_again = input("Would you like to make another order? ")
    if order_again.lower() in ['y', 'yes', 'continue']:
        clear_screen()
    else:
        ordering = False

print(f"Total Order Price: {total_price:.2f}")
print(f"Your Order: {customer_order}")