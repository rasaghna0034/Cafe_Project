# Cafe Management System

menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 80,
    "Burger": 100,
    "Pasta": 120,
    "Cake": 60
}

order = {}

def display_menu():
    print("\n------ Cafe Menu ------")
    for item, price in menu.items():
        print(f"{item:10} : ₹{price}")
    print("------------------------\n")

def take_order():
    while True:
        item = input("Enter item name to order (or 'done' to finish): ").title()
        if item.lower() == 'done':
            break
        elif item in menu:
            qty = int(input(f"Enter quantity for {item}: "))
            if item in order:
                order[item] += qty
            else:
                order[item] = qty
        else:
            print("Item not on the menu. Please try again.")

def generate_bill():
    print("\n------ Bill ------")
    total = 0
    for item, qty in order.items():
        price = menu[item] * qty
        print(f"{item:10} x {qty} = ₹{price}")
        total += price
    tax = round(total * 0.05, 2)
    grand_total = total + tax
    print(f"\nSubtotal   : ₹{total}")
    print(f"Tax (5%)   : ₹{tax}")
    print(f"Total Bill : ₹{grand_total}")
    print("------------------")
    print("Thank you! Visit Again.\n")

# Main Program
print("\nWelcome to 'The cafe Lounge !")
display_menu()
take_order()
if order:
    generate_bill()
else:
    print("No items ordered.")
