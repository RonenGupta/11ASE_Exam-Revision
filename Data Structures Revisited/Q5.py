undo_stack = []
while True:
    sig = str(input("Hello and welcome to the stack! Choose between type, undo and exit: "))
    if sig == 'type':
        val = str(input("What do you want to type: "))
        print(f'Added {val} to the stack!')
        undo_stack.append(val)
    elif sig == 'undo':
        if not undo_stack:
            print("Theres nothing in the stack!")
        else:
            undo = undo_stack.pop()
            print(f'Popped {undo} from the stack!')
    elif sig == 'exit':
        print('Thanks for visiting the stack!')
        break    