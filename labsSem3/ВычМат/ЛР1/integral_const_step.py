from menu import *
from math import *


a = 1.9
b = 2.6
result = None


def integral(arg):
    return (sqrt(2 * arg + 1.7) / (2.4 + sqrt(1.2 * arg * arg + 0.6)))


def integral_const_step_left(n):

    ''' Функция вычсления интеграла
        методом левых прямоугольников
        с постоянным шагом '''

    print("Вычисляется левыми частями переменным шагом")
    global result
    global a

    global b
    s = 0
    h = (b - a) / n
    x = a
    while (x <= (b - h)):
        s += integral(x)
        x += h
    result = h * s
    print("Шаг вычислений равен " + str(h))
    return result



def integral_const_step_right(n):

    ''' Функция вычсления интеграла
        методом правых прямоугольников
        с постоянным шагом '''

    print("Вычисляется правыми частями постоянным шагом")
    global result
    global a

    global b
    s = 0
    h = (b - a) / n
    x = a + h
    while (x <= b):
        s += integral(x)
        x += h
    result = h * s
    print("Шаг вычислений равен " + str(h))

    return result


def integral_const_step_trap(n):

    ''' Функция вычсления интеграла
        методом трапеций с постоянным шагом '''

    print("Вычисляется трапециями постоянным шагом")

    global result
    global a
    global b

    s = 0
    h = (b - a) / n
    x = a + h

    while (x <= b):
        s += integral(x)
        x += h

    result = h * ((integral(a) + integral(b)) / 2 + s)
    print("Шаг вычислений равен " + str(h))

    return result


def integral_const_step_simpson(n):

    ''' Функция вычсления интеграла
        методом симпсона с постоянным шагом '''

    print("Вычисляется симпсоном постоянным шагом")

    global result
    global a
    global b

    s1 = 0
    s2 = 0
    h = (b - a) / n / 2

    x = a + h
    while (x <= b):
        s1 += integral(x)
        x += 2 * h

    x = a + 2 * h
    while (x <= (b - h)):
        s2 += integral(x)
        x += 2 * h

    result = h / 3 * (integral(a) + integral(2 * b) + 4 * s1 + 2 * s2)
    print("Шаг вычислений равен " + str(h))

    return result


def integral_double_recount_1(n):

    ''' Функция вычсления интеграла
        методом правых прямоугольников
        с переменным шагом без смещения '''

    print("Вычисляется левыми частями переменным шагом")

    global a
    global b

    I_n = 0
    I_2n = 0
    R = 1

    E = float(input("Введите точность\n"))

    while (R > E):
        S2 = 0
        h = (b - a) / n
        x = a
        while (x <= (b - h)):
            S2 += integral(x)
            x += h
        I_2n = h * S2
        R = abs(I_2n - I_n)
        I_n = I_2n
        h = h / 2
    print("Шаг вычислений равен " + str(h))

    return (I_2n)


def integral_double_recount_2(n):

    ''' Функция вычсления интеграла
        методом правых прямоугольников
        с переменным шагом со смещением '''

    print("Вычисляется левыми частями переменным шагом")

    global a
    global b

    E = float(input("Введите точность\n"))
    hv = (b - a) / n
    hs = a
    hd = hv
    I1 = 0
    R = 1
    x = a

    while R > E:
        x = hs
        s = 0
        while x <= (b - hv):
            s += integral(x)
            x += hd
        I2 = hd * s
        R = abs(I1 - I2)
        I1 = I2
        if hd == hv:
            hd = hv / 2
            hv /= 4
        else:
            hd = hv
            hs = hd / 2
            hv /= 2
    print("Шаг вычислений равен " + str(h))

    return I2
