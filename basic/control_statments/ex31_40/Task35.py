number = 1243

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)

if miavor * tasnavor == 12:
    print("y=12")
else:
    print("y=0")
