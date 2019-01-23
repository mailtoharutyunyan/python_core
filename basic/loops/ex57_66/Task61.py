N = 8125486
count = 0
n = N

while n > 0:
    n = int(n / 10)
    count += 1

count = int(pow(10, count - 1))
while count >= 1:
    print(N / count)
    N = int(N % count)
    count = int(count / 10)
