from math import sqrt

for i in reversed(range(1000, 9999)):
    sqrt1 = int(sqrt(i * 18))
    if sqrt1 * sqrt1 == i * 18:
        print(i)
        break



