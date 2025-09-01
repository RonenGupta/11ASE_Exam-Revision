def calc_pizza(size, topping_amt):
    price = 10
    if size.lower() == 'small':
        price += 0
    elif size.lower() == 'medium':
        price += 2
    elif size.lower() == 'large':
        price += 4
    price += topping_amt * 1.50
    return price
   
pizza_list = {}
while True:

    choice = input("Order or Exit: ")
    if choice.lower() == "order":
        name = input("Hello, welcome to the pizza shop, what pizza would you like: ")
        size = input("What size: ")
        while size.lower() not in ['small', 'medium', 'large']:
            size = input("What size: ")
        topping_amt = input("How many toppings: ")
        while not topping_amt.isdigit():
            topping_amt = input("How many toppings: ")
        topping_amt = int(topping_amt)
        print(f"You ordered {name} which costs {calc_pizza(size, topping_amt)}")
        pizza_list[name] = calc_pizza(size, topping_amt)
    elif choice.lower() == 'exit':
        print("Thank you for visiting the pizza shop!")
        print("Your order:")
        for name, price in pizza_list.items():
            print(f"{name}: {price}")
        break