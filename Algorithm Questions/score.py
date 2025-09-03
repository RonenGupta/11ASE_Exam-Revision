scores = [3,5,5,2,1,4,0,1,4,5]
points = []
print("Round   Score   Points")

for i in range(len(scores)):

    if scores[i] == 5 and i != len(scores) - 1:
        points.append(scores[i] + scores[i + 1])
        print(f"{i + 1}       {scores[i]}       {points[i]}")

    elif scores[i] == 5 and i == len(scores) - 1:
        points.append(scores[i] + 5)
        print(f"{i + 1}      {scores[i]}       {points[i]}")

    else:
        points.append(scores[i])
        print(f"{i + 1}       {scores[i]}       {points[i]}")

print(f"TOTAL POINTS: {sum(points)}")