# СИСТЕМЫ СЧИСЛЕНИЯ(-36 до 36)
def convert_base(num, from_base, to_base):
    n = int(str(num), from_base)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


# ДЕЛИТЕЛИ ЧИСЛА
def dividers(a):
    arr = []
    for i in range(2, a):
        if a % i == 0:
            arr.append(i)
    return arr


# ОСТАВЛЯЕТ УНИКАЛЬНЫЕ ЗНАЧЕНИЯ МАССИВА
def unique(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


# ПРОСТЫЕ ЧИСЛА
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


# НЕЧЕТНЫЕ ЦИФРЫ ЧИСЛА
def odd(a):
    a = int(a)
    odd = 0
    while a > 0:
        if a % 2 != 0:
            odd += 1
        a = a // 10
    return odd


# ЧЕТНЫЕ ЦИФРЫ ЧИСЛА
def even(a):
    a = int(a)
    even = 0
    while a > 0:
        if a % 2 == 0:
            even += 1
        a = a // 10
    return even


# ФАКТОРИАЛ ЧИСЛА
def factorial(num):
    count = 2
    for i in range(3, num + 1):
        count *= i
    return count

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
