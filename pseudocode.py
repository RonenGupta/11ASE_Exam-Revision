import numpy as np

def Search(SearchItem):
    ItemArray = np.array([42, 64, 23, 21, 65, 12])
    found = False
    LastIndex = len(ItemArray)
    Index = 1
    while found == False and Index < LastIndex + 1:
        if ItemArray[Index - 1] == SearchItem:
            found = True
        else:
            Index += 1
    if found == True:
        return 'Position', Index
    else:
        return 'Not found'
    
print(Search(12))