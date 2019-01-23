number = 1243

miavor = int(number % 10)
hazaravor = int(number / 1000)

if miavor == 4 and hazaravor == 4:
    print("yes")
else:
    print("no")
