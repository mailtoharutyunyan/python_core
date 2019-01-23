from math import sqrt

n = 14

for i in range(100, 1000):
    if sqrt(i) > n:
        print(i)
        break
