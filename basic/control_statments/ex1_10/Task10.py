a = 4444
b = 8
c = 99
temp = None

if a < c:
    temp = a
    a = c
    c = temp

if b < c:
    temp = b
    b = c
    c = temp

if a < b:
    temp = b
    b = a
    a = temp

print(a, b, c)
