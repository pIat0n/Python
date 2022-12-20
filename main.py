# перевод систем счисления
def convert_base(num: int, from_base: int, to_base: int):
    n = int(str(num), from_base)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


# делители числа
def dividers(num: int):
    arr = []
    for i in range(2, num):
        if num % i == 0:
            arr.append(i)
    return arr


# оставляет уникальные значения массива
def unique(num: str):
    unique = []
    for number in num:
        if number not in unique:
            unique.append(number)
    return unique


# проверка на простату
def is_prime(num: int):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


# количество нечетных цифр числа
def odd(num: int):
    odd = 0
    while num > 0:
        if num % 2 != 0:
            odd += 1
        num = num // 10
    return odd


# количество четных цифр числа
def even(num: int):
    even = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        num = num // 10
    return even


# сумма цифр числа
def summa(num: str):
    return sum(map(int, str(num)))
