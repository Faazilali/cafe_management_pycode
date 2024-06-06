menu={'Pizza':40, 'Pasta':50, 'Burger':60, 'Salad':70, 'Coffee':80}

print("Welcome to the Cafe")
print("Cafe Menu:")
print("Pizza:40\nPasta:50\nBurger:60\nSalad:70\nCoffee:80")

order_total=0

item1=input("Enter the item you want to order:")
if item1 in menu:
    order_total+=menu[item1]
    print(f"Your {item1} is added in your order.")
else:
    print(f"{item1} is not available.")

ask=input("Want to add another item?")
if ask=='yes':
    item2=input("Enter another item:")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"{item2} has been added.")
    else:
        print(f"{item2} is not available.")

print("Total amount of your order is",order_total)