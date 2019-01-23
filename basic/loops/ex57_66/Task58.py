N = 8945

summa = 0

while N > 0:
    summa = int(summa + N % 10)
    N = int(N / 10)
print(summa)
