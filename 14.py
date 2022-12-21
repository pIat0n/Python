for i in range(0, 37):
    y = int('123' + str(i))
    # print("Первое число: ", y)
    x = int(str(y)[0]) * 37 ** 3 + int(str(y)[1]) * 37 ** 2 + int(str(y)[2]) * 37 + int(str(y)[3])
    # print("Первое число в десятичной системе: ", x)
    z = int('4' + str(i) + '59')
    # print('Второе число :', z)
    c = int(str(z)[0]) * 37 ** 3 + int(str(z)[1]) * 37 ** 2 + int(str(z)[2]) * 37 + int(str(z)[3])
    # print('Второе число в десятичной системе: ', c)
    if (x + c) % 36 == 0:
        print(((x + c) // 36))
