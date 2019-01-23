n = 16
y = 0

if n % 4 == 0:
    for i in range(1, int(n / 2)):
        if pow(4, i) == n:
            y = 1
print(y)
