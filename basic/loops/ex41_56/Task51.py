from math import sqrt

for i in range(1000, 10000):
    sqrt1 = int(sqrt(i * 26))
    if sqrt1 * sqrt1 == i * 26:
        print(i)
        break
