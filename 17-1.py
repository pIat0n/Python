from main import *

file = open("17-1.txt")
l = [int(i) for i in file]
count = 0
summa = []
srednee = sum(l) // len(l)
for i in range(len(l) - 2):
    if l[i] < srednee or l[i + 1] < srednee or l[i + 2] < srednee:
        if str(l[i]).count("2") != 0 and str(l[i + 1]).count("2") != 0 or str(l[i]).count("2") != 0 and str(l[i + 2]).count("2") != 0 or str(l[i + 1]).count("2") != 0 and str(l[i + 2]).count("2") != 0:
            count += 1
            summa.append(l[i] + l[i + 1] + l[i + 2])
print(count, max(summa))

a = 3 * 125 ** 6 + 2 * 25 ** 9 + 5 ** 12 - 625
print(convert_base(a, 10, 5))
