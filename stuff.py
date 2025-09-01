def calc_pizza(name, size, topping_amt):
    price = 10
    if size.lower() == 'small':
        price += 0
    elif size.lower() == 'medium':
        price += 2
    elif size.lower() == 'large':
        price += 4
    price += topping_amt * 1.50
    return f"Your {name} costs {price}!"

while True:
    choice = input("Order or Exit")
    if choice == "Order":
name = input("Hello, welcome to the pizza shop, what pizza would you like: ")
size = input("What size: ")
topping_amt = int(input("How many toppings: "))
