number = 1562

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100 % 10)
hazaravor = int(number / 1000)

if miavor * tasnavor * haryuravor * hazaravor > 200:
    print(0)
else:
    print(1)
