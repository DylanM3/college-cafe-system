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

def calculate_discount(total_price):
    if total_price > 10:
        print("Orders over £10 qualify for 10% discount")
        total_price = total_price * 0.9
        print(f"Total Price (after discounts): {total_price:.2f}")
        return total_price