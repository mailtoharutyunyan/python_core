a = 3
b = 1
c = 5

temp = None

if a > c:
    temp = a
    a = c
    c = temp
elif b > c:
    temp = b
    b = c
    c = temp
elif a > b:
    temp = b
    b = a
    a = temp

    print(a, b, c)
