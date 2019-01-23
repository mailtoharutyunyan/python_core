number = 642

miavor = int(number % 10)
tasnavor = int(number % 100 / 10)
haryuravor = int(number / 100)

maximum = miavor

if tasnavor > maximum:
    maximum = tasnavor

if haryuravor > maximum:
    maximum = haryuravor

print(maximum)
