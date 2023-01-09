# перевод систем счисления
def convert_base(num, from_base, to_base):
    n = int(str(num), from_base)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


# делители числа
def dividers(num):
    arr = []
    for i in range(2, num):
        if num % i == 0:
            arr.append(int(i))
    return arr


# уникальные значения строки
def unique(num):
    arr = []
    for number in num:
        if number not in arr:
            arr.append(int(number))
    return arr


# проверка на простату
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


# количество нечетных цифр числа
def odd(num):
    answer = 0
    while num > 0:
        if num % 2 != 0:
            answer += 1
        num = num // 10
    return answer


# количество четных цифр числа
def even(num):
    answer = 0
    while num > 0:
        if num % 2 == 0:
            answer += 1
        num = num // 10
    return answer


# сумма цифр числа
def summa(num):
    answer = []
    for i in str(num):
        answer.append(int(i))
    return sum(answer)


# сортировка пузыриком
def sorting(array):
    length = len(array)
    for i in range(0, length):
        for y in range(0, length - i - 1):
            if array[y] > array[y + 1]:
                temp = array[y]
                array[y] = array[y + 1]
                array[y + 1] = temp
