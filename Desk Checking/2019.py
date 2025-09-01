x = 1
y = int(input("Whats the value of y"))
while x <= 8:
    z = y
    if x < 7:
        x += 1
        if x < 8:
            print(x*z)
    x += 1
print("Done")