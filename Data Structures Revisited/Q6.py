phone_book = {}

while True:
    print("Hello and welcome to the phone book!")
    val = input("Would you like to add, view, or delete a contact: ")
    if val.lower() == 'add':
        name = input("Enter a name to add: ")
        phone = input("Enter the phone number: ")
        phone_book[name] = phone
        print(f"Added {name} with phone no. {phone} to the phonebook!")
        
    elif val.lower() == 'view':
            name1 = input("Enter a name to find their number: ")
            if name1 not in phone_book:
                 print(f"{name1} is not in your phonebook!")
            else:
                 print(phone_book[name1])

    elif val.lower() == 'delete':
         delete = input('Enter a name to delete from the phonebook: ')
         if delete not in phone_book:
              print(f"{delete} is not in your phonebook!")
         else:
              del phone_book[delete]
              print(f"{delete} has been deleted from the phonebook!")