number = 142

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100)

k = 150

if number > k:
    print(number / (miavor + tasnavor + haryuravor))
else:
    print(number / miavor)
