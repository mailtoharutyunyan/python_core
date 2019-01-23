N = 465
p = 1

while N > 0:
    p = int(p * (N % 10))
    N = int(N / 10)

print(p)
