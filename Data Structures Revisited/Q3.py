array = ["milk", "bread", "eggs"]

while True:
    choice = input("Welcome to the sigma shtua please enter your choice,a")
    if choice.lower() == 'append':
        val = str(input("What d u wanna append sjn?"))
        array.append(val)
        print(f"I append ts {val} now go away bviggy")

    elif choice.lower() == 'remove':
        val = str(input("wha do u wanna renove fam"))
        array.remove(val)
        print(f"Ok twin i remoged {val}")

    elif choice.lower() == 'view':
        print(array)

    elif choice.lower() == 'exit':
        print("ok twin i leave now goodyee")
        break