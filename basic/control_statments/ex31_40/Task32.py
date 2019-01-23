number = 1986

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100 % 10)
hazaravor = int(number / 1000)

if number < 5000:
    print(number / (miavor + haryuravor))
else:
    print(number / (tasnavor + hazaravor))
