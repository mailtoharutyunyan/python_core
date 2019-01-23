from math import sqrt

for i in range(100, 1000):
    sqrt1 = int(sqrt(i * 16))
    if sqrt1 * sqrt1 == i * 16:
        print(i)
        break
