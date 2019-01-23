number = 8610

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100 % 10)
hazaravor = int(number / 1000)

if miavor == 1 or tasnavor == 1 or haryuravor == 1 or hazaravor == 1:
    print(1)
else:
    print(0)
