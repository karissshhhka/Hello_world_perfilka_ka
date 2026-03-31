A, B, C, D = float(input()), float(input()), float(input()), float(input())

min_val = A

if B < min_val:
    min_val = B

if C < min_val:
    min_val = C

if D < min_val:
    min_val = D

print(min_val)
