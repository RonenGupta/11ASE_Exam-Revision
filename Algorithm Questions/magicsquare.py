import numpy as np

magic_square = np.array([[2, 7, 6],     # 0 0 | 0 1 | 0 2
                         [9, 5, 1],     # 1 0 | 1 1 | 1 2
                         [4, 3, 8]])    # 2 0 | 2 1 | 2 2

def check_magic(square):
    for i in range(0, 3):
        if square[i][0] + square[i][1] + square[i][2] == 15:
            pass
        else:
            return False
        if square[0][i] + square[1][i] + square[2][i] == 15:
            pass
        else:
            return False
    if square[0][0] + square[1][1] + square[2][2] == 15:
        pass
    else:
        return False
    if square[0][2] + square[1][1] + square[2][0] == 15:
        pass
        return True
    else:
        return False
print(check_magic(magic_square))