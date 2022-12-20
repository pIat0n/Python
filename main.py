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
            arr.append(int(i))
    return arr


# уникальные значения строки
def unique(num: str):
    arr = []
    for number in num:
        if number not in arr:
            arr.append(int(number))
    return arr


# проверка на простату
def is_prime(num: int):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


# количество нечетных цифр числа
def odd(num: int):
    answer = 0
    while num > 0:
        if num % 2 != 0:
            answer += 1
        num = num // 10
    return answer


# количество четных цифр числа
def even(num: int):
    answer = 0
    while num > 0:
        if num % 2 == 0:
            answer += 1
        num = num // 10
    return answer


# сумма цифр числа
def summa(num: str):
    return sum(map(int, num))
