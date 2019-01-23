number = 142

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100)

if miavor > tasnavor:
    print(number / (miavor + tasnavor + haryuravor))
else:
    print(number)
