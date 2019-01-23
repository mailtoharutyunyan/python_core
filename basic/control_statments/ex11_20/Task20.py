a = 3
b = 13
c = 12
d = 24

temp = None

if a < b:
    temp = b
    b = a
    a = temp
if a < c:
    temp = a
    a = c
    c = temp
if a < d:
    temp = a
    a = d
    d = temp
if b < c:
    temp = b
    b = c
    c = temp
if b < d:
    temp = b
    b = d
    d = temp
if c < d:
    temp = c
    c = d
    d = temp

print(a, b, c, d)
