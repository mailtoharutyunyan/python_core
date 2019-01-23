number = 9285

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100 % 10)
hazaravor = int(number / 1000)

if miavor + tasnavor + haryuravor + hazaravor > 20:
    print(1)
else:
    print(0)
