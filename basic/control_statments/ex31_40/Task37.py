number = 4564

miavor = int(number % 10)
tasnavor = int(number / 10 % 10)
haryuravor = int(number / 100 % 10)
hazaravor = int(number / 1000)

if number == pow((miavor + tasnavor + hazaravor + hazaravor), 2):
    print("Yes")
else:
    print("No")
