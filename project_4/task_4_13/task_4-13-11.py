array = [2, 3, 5, 8, 9, 11]
n = len(array)
k = 0
sum = 0

for i in range(n):
  if i % 2 == 0:
    k += 1
    sum += array[i]
zn = sum / k
print(round(zn, 2))  
