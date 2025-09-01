import numpy as np

baaaaaa = np.array([[2, 7, 6],
                      [9, 6, 1],
                      [4, 3, 7]])

def squarespace(baaaaaa):
    for i in range(3):
        if baaaaaa[i][0] + baaaaaa[i][1] + baaaaaa[i][2] == 15:
            if baaaaaa[0][i] + baaaaaa[1][i] + baaaaaa[2][i] == 15:
                if baaaaaa[0][0] + baaaaaa[1][1] + baaaaaa[2][2] == 15:
                    if baaaaaa[0][2] + baaaaaa[1][1] + baaaaaa[2][0] == 15:
                        return True

print(squarespace(baaaaaa))

