number = 198

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100)

if haryuravor < tasnavor:
    temp = haryuravor
    haryuravor = tasnavor
    tasnavor = temp

if tasnavor < miavor:
    temp = miavor
    miavor = tasnavor
    tasnavor = temp

if haryuravor < tasnavor:
    temp = haryuravor
    hundreds = tasnavor
    tens = temp

print(haryuravor, tasnavor, miavor)
