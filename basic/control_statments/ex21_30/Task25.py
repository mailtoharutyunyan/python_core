number = 142

miavor = number % 10
tasnavor = number / 10 % 10
haryuravor = number / 100

minimum = miavor

if tasnavor < minimum:
    minimum = tasnavor

if haryuravor < minimum:
    minimum = haryuravor

print(minimum)
