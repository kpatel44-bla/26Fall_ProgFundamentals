#Store the cafe name and sales tax rate
cafe_name = "Python Café"
tax_rate = 0.08

# Store menu items and their prices in a dictionary
menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25
}

# Start with an empty customer order
order = []
def greet(name):#welcome the customers
    print(f"Welcome to {cafe_name}, {name}!")


def show_menu(menu):#display the menu items and their prices
    print("--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def show_order(order, menu):#display the items in the customer's order and their prices
    if len(order) == 0:
        print("Your order is empty.")
    else:
        print("--- YOUR ORDER ---")
        for item in order:
            print(f"{item}: ${menu[item]:.2f}")
        print(f"Items: {len(order)}")


def calculate_subtotal(order, menu):
    subtotal = 0
    for item in order:
        subtotal = subtotal + menu[item]
    return subtotal
def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20:
        discount = subtotal * 0.15
    elif is_member and subtotal >= 10:
        discount = subtotal * 0.10
    elif not is_member and subtotal >= 25:
        discount = subtotal * 0.05
    else:
        discount = 0
    return discount


# Print the receipt with discount, tax, and final total
def print_receipt(name, order, menu, is_member):
    subtotal = calculate_subtotal(order, menu)
    discount = get_discount(subtotal, is_member)
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax

    print(f"Receipt for {name}:")
    for item in order:
        print(f"{item}: ${menu[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    if not is_member:
        print("Join our rewards club for more discounts!")
    print(f"Thanks for visiting, {name}!")


# Ask for customer information
print(f"*** {cafe_name} ***")
name = input("What's your name? ")
greet(name)
member_answer = input("Are you a rewards member? (yes/no) ").lower()
is_member = member_answer == "yes"

# Keep showing options until the customer checks out
while True:
    print("\n1. View menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. View my order")
    print("5. Checkout")
    choice = input("Choose an option (1-5): ")

    if choice == "1":# Respond to the selected menu option
        show_menu(menu)
    elif choice == "2":
        item = input("What would you like? ").lower()
        if item in menu:
            quantity = int(input("How many? "))
            if quantity >= 1:
                for number in range(quantity):
                    order.append(item)
                print(f"Added {quantity} {item} to your order.")
            else:
                print("Quantity must be at least 1.")
        else:
            print("That item is not on the menu.")
    elif choice == "3":
        item = input("Which item should I remove? ").lower()
        if item in order: # Remove only one copy of this item
            order.remove(item)
            print(f"Removed one {item}.")
        else:
            print("That item is not in your order.")
    elif choice == "4":
        show_order(order, menu)
    elif choice == "5":
        if len(order) == 0:
            print("Please add something to your order first.")
        else: #calculate and display the receipt and endf the loop
            print_receipt(name, order, menu, is_member)
            break
    else:
        print("Please choose a number from 1 to 5.")
