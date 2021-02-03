from math import *
from menu import a, b, integral


def integral_const_step_left(n):

    ''' Функция вычсления интеграла
        методом левых прямоугольников
        с постоянным шагом '''

    print("Вычисляется левыми частями постоянным шагом")
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

    ''' Функция вычсления интеграла методом трапеций с постоянным шагом '''

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

    ''' Функция вычсления интеграла методом симпсона с постоянным шагом '''

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
    I_2n = 0


def integral_double_recount_1(n):

    ''' Функция вычсления интеграла
        методом левых прямоугольников
        с переменным шагом без смещения '''

    print("Вычисляется левыми частями переменным шагом")

    global a
    global b

    I_n = 0
    I_2n = 0
    R = 1
    E = float(input("Введите точность\n"))

    h = (b - a) / n

    while (R > E):
        S2 = 0

        x = a
        while (x <= (b - h)):
            S2 += integral(x)
            x += h
        I_2n = h * S2
        R = abs(I_2n - I_n)
        I_n = I_2n
        h = h / 2

    print('------------------')
    print("n = ", n)
    print("e = ", e)
    print("Шаг вычислений равен " + str(h + h))
    return (I_2n)


def integral_double_recount_2(n, E):

    ''' Функция вычсления интеграла
        методом левых прямоугольников
        с переменным шагом со смещением '''

    print("Вычисляется левыми частями переменным шагом")

    global a
    global b

    s = 0
    I1 = 0
    I2 = 0
    hv = (b - a) / n
    hs = hv
    hd = hv
    R = 1 + E
    x = a
    # E = float(input("Введите точность\n"))
    # всё хуйня давай по новой
    while (R > E):
        while (x < (b - hs)): 
            x += hd
            s += integral(x)
    
        s += integral(x + hd)
        I2 = hs * 2 * s
        R = abs(I2 - I1)
        I1 = I2
        hs = hd / 2
        hd = hd / 2
        x = a + hs
        s = 0

    print('------------------')
    print("n = ", n)
    print("e = ", E)
    print("Шаг вычислений равен " + str(hs))
    return (I2)


if __name__ == "__main__":
    print(integral_double_recount_2(10, 10**-6))
    print(integral_double_recount_2(100, 10**-6))
    print(integral_double_recount_2(1000, 10**-6))
    print(integral_double_recount_2(10000, 10**-6))
