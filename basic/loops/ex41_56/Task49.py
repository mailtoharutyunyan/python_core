p = 1

for i in range(100, 1000):
    if (i % 3 == 1) and (i % 4 == 2):
        p = p * i

print(float(p))
