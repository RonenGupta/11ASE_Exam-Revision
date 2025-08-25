import numpy as np

temperatures = np.array([12, 14, 56, 71, 12, 45, 53])

for i in range(7):
    temps = int(input(f"Enter the {i + 1} temp u fatty: "))
    temperatures[[i]] = [temps]

mean_temperature = np.mean(temperatures)
max_temperature = np.max(temperatures)
min_temperature = np.min(temperatures)

print(f"Minimum Temp: {min_temperature}")
print(f"Max Temp: {max_temperature}")
print(f"Mean Temp: {mean_temperature}")