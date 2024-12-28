menu = {
    'pizza': 90,
    'pasta': 50,
    'Burger': 70,
    'salad': 90,
    'coffee': 80,
}

print("Welcome to our Restaurant")
print("pizza Rs90\npasta Rs50\nBurger Rs70\nsalad Rs90\ncoffee Rs80")
order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Order item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Order item {item_2} is not available")

print(f"The total amount for your order is Rs{order_total}")
