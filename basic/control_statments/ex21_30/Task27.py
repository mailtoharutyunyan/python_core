number = 282

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100)

if number > 300:
    print(tasnavor / miavor)
else:
    print(haryuravor / miavor)
