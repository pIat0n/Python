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
def de(n):
    arr = []
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            arr.append(i)
    return arr


# УНИКАЛЬНЫЕ ЗНАЧЕНИЯ МАССИВА
def unique(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


# ПРОСТЫЕ ЧИСЛА
def is_prime(n):
    if n == 0:
        return True
    d = 2
    while n % d != 0:
        d += 1
    return d == n


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


'''

answers = []
for question in range(0, 9 + 1):
    for star1 in range(0, 9 + 1):
        for star2 in range(0, 9 + 1):
            for star3 in range(0, 9 + 1):
                    a = f"1{question}49341"
                    b = f"1{question}493{star1}41"
                    c = f"1{question}493{star1}{star2}41"
                    d = f"1{question}493{star1}{star2}{star3}41"
                    if int(a) < 10 ** 10:
                        if int(a) % 2023 == 0:
                            answers.append(int(a))
                    if int(b) < 10 ** 10:
                        if int(b) % 2023 == 0:
                            answers.append(int(b))
                    if int(c) < 10 ** 10:
                        if int(c) % 2023 == 0:
                            answers.append(int(c))
                    if int(d) < 10 ** 10:
                        if int(d) % 2023 == 0:
                            answers.append(int(d))
    answers.sort()
    unique_answers = []
    for answer in answers:
        if answer not in unique_answers:
            unique_answers.append(answer)
    print(unique_answers)

'''

answers = []
for i in range(173225, 217437 + 1):
    for y in de(i):
        if is_prime(y):
            answers.append(y)
print(answers)