# СИСТЕМЫ СЧИСЛЕНИЯ
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
