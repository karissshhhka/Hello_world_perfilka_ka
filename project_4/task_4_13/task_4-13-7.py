array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)

sum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum += array[j]

zn = sum / n
print(round(zn, 2))
