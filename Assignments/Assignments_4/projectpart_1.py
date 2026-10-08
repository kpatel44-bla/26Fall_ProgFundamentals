# Python Cafe Project - Part 1

cafe_name = "Python Cafe"
tax_rate = 0.08

menu = {
    "coffee": 3.00,
    "tea": 2.50,
    "latte": 4.00,
    "muffin": 3.50
}

order = []


def welcome():
    print("========================")
    print("Welcome to", cafe_name)
    print("========================")


def show_menu(cafe_menu):
    print("--- MENU ---")

    for item, price in cafe_menu.items():
        print(f"{item}: ${price:.2f}")


def show_order(customer_order, cafe_menu):
    if len(customer_order) == 0:
        print("Your order is empty.")
    else:
        print("--- YOUR ORDER ---")

        for item in customer_order:
            print(f"{item}: ${cafe_menu[item]:.2f}")

        print(f"Items: {len(customer_order)}")


def calculate_subtotal(customer_order, cafe_menu):
    subtotal = 0

    for item in customer_order:
        subtotal = subtotal + cafe_menu[item]

    return subtotal

welcome()
show_menu(menu)

customer_name = input("Enter your name: ")

item1 = input("Enter an item: ").lower()
order.append(item1)

item2 = input("Enter another item: ").lower()
order.append(item2)

show_order(order, menu)

subtotal = calculate_subtotal(order, menu)
tax = subtotal * tax_rate
total = subtotal + tax

print("--- RECEIPT ---")
print(f"Customer: {customer_name}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("Thank you for visiting", cafe_name)