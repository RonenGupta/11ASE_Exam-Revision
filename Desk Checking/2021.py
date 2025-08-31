list = [33, 38, 40, 44, 50, 60, 75]
low = 1
high = 7
found = False
SearchItem = int(input("SearchItem: "))
while found == False and high > low:
    index = low + high
    index = int(index / 2)
    print(index)
    if SearchItem == list[index]:
        found = True
    else:
        if SearchItem < list[index]:
            high = round(index) #
        else:
            low = round(index) #
if found == True:
    print("Found at ", index + 1)
else:
    print("Not found")