N = 13456789

while N > 0:
    if N % 10 == 2:
        print("true")
    else:
        N = N / 10
print("false")
