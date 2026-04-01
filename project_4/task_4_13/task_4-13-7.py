array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)
sum = 0

for i in range(n):
    sum += array[i]

zn = sum / n
print(round(zn, 2))
