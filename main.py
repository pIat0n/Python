# СИСТЕМЫ СЧИСЛЕНИЯ
def convert_base(num, to_base=10, from_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


# ДЕЛИТЕЛИ ЧИСЛА
def dividers(a):
    arr = []
    for i in range(a - 1, 1, -1):
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
def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


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
