N = int(input("Введите количество чисел: "))

A = []
for i in range(N):
    A.append(float(input(f"Введите число {i+1}: ")))

k = 1
Nmax = 0

for i in range(1, N):
    if A[i] == A[Nmax]:
        k += 1
    if A[i] > A[Nmax]:
        Nmax = i
        k = 1

print(A[Nmax])
