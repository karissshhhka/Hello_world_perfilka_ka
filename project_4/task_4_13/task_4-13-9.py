array = [2, 3, 5, 8, 9, 11]
n = len(array)
sum = 0

for i in range(n):
  if array[i] % 2 != 0:
    sum += array[i]
print(sum)  
