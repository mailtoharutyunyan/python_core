
p = 1

for i in range(100, 1000):
    if i % 2 != 0 and i % 3 != 0:
        p = p * i

print(p)
