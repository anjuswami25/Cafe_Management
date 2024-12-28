menu = {
    'pizza': 90,
    'pasta': 50,
    'Burger': 70,
    'salad': 90,
    'coffee': 80,
}

print("Welcome to our Restaurant")
print("pizza Rs90\npasta Rs50\nBurger Rs70\nsalad Rs90\ncoffee Rs80")
order_total = 0  # Initialize the total

# Normalize input to lowercase for case-insensitivity
item_1 = input("Enter the name of item you want to order = ").strip().lower()
if item_1 in map(str.lower, menu.keys()):  # Check case-insensitive match
    for key in menu:  # Find the actual key in the dictionary
        if key.lower() == item_1:
            order_total += menu[key]
            print(f"Your item {key} has been added to your order")
            break
else:
    print(f"Order item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of second item = ").strip().lower()
    if item_2 in map(str.lower, menu.keys()):  # Check case-insensitive match
        for key in menu:  # Find the actual key in the dictionary
            if key.lower() == item_2:
                order_total += menu[key]
                print(f"Item {key} has been added to your order")
                break
    else:
        print(f"Order item {item_2} is not available")
print(f"The total amount for your order is Rs{order_total}")

