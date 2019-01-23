p = 1

for i in range(10, 100):
    if i % 3 == 0 and i % 5 == 0:
        p = p * i
print(p)
