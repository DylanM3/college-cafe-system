import os

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# CLEAR SCREEN FOR CORRECT OPERATING SYSTEM
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# GREET CUSTOMER
def greet_customer():
    customer_name = input("What is your name? ")
    print() # Formatting

    print(f"{customer_name}, welcome to PyCafe!")
    print("We hope you are hungry for a Byte.")
    return customer_name

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
