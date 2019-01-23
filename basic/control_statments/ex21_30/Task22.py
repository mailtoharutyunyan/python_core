number = 443

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100)

if miavor == tasnavor or miavor == haryuravor or tasnavor == haryuravor:
    print("true")
else:
    print("false")
