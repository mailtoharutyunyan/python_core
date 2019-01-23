number = 1235

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100 % 10)
hazaravor = int(number / 1000)

if miavor > tasnavor:
    print(miavor * haryuravor)
else:
    print(1)
