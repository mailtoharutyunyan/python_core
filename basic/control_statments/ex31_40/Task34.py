number = 1223

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)

if miavor + tasnavor == 5:
    print('s')
else:
    print('d')
