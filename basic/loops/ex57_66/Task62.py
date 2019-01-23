N = 123456789
newN = 0
count = 0
n = N

while n > 0:
    n = n / 10
    count += 1
count = int(pow(10, count - 1))
while N > 0:
    newN = int(newN + N % 10 * count)
    count = count / 10
    N = N / 10

print(newN)
# TODO error
