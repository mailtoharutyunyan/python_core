number = 249

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100)

if tasnavor + haryuravor < 5:
    print(chr(102))  # f
else:
    print(chr(98))  # b
