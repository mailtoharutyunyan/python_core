a = 1
b = 2
c = 3

minimum = 0

if a < b and a < c:
    minimum = a
elif b < a and b < c:
    minimum = b
elif c < a and c < b:
    minimum = c

print(minimum)
