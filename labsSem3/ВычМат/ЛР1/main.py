from integral_const_step import *
from math import *
import sys

a = 1.9
b = 2.6
result = None

def integral(arg):
    return (sqrt(2 * arg + 1.7) / (2.4 + sqrt(1.2 * arg * arg + 0.6)))

def menu():
    global result

    choice_type = int(input("Введите тип решаемой задачи:\n1 - Вычисление интеграла"))
    if choice_type == 1:
        integral_menu()

    print("Полученный результат: ", result)

    print("Завершить работу программы?\n"
        "y - Да\n"
        "n - Начать сначала\n")

    choice = input()

    if choice == 'y' or choice == 'Y':
        sys.exit()

    else:
        menu()
        return

def integral_menu():

    global result

    # Словарь с доступными методами вычислений
    choise_method_list = {
        1: "Метод прямоугольников левых частей",
        2: "Метод прямоугольников правых частей",
        3: "Метод трапеций",
        4: "Метод парабол",
        5: "Вернуться на главную",
    }

    # Вывод этих методов
    print('Выберите метод решения:')
    for i in range(1, 6):
        print(i, ":", choise_method_list[i])

    # Пользователь выбирает метод
    choice_method = int(input())


    # Если пользователь выбрал несуществующий пункт, перезапускаем функцию
    if (choice_method < 1 and choice_method > 6):
        print("Выбран неверный пункт! Попробуйте снова\n")
        integral_menu()
        return

    # Для метода прямоульгоников левых частей доступны алгоритмы с переменными
    # Поэтому проверяем выбрал ли пользователь метод прямоугольников левых частей
    # И создаём словарь с доступными алгоритмами для данного метода
    elif choice_method == 1:

        choice_algorithm_list = {
        1: "С постоянным шагом",
        2: "Двойной пересчёт без смещение",
        3: "Двойной пересчёт со смещением"

    }

    # Возвращаемся в главное меню, если нужно
    elif choice_method == 5:

        menu()
        return

    # Создаём словарь с доступными алгоритмами для остальных методов
    else:

        choice_algorithm_list = {
            1: "С постоянным шагом"
        }


    # Получаем список всех ключей созданного словаря
    # И делаем по ним проход, выводя значения,
    # Соответствующие этим ключам
    for i in choice_algorithm_list.keys():
        print(i, ':', choice_algorithm_list[i])

    # Запрашиваем у пользователя нужный алгоритм
    choice_algorithm = int(input())


    # Создаём словарь с существующими действиями на основе выбора
    # Методов и алгоритмов пользователем и вызываем
    # Соответстующую выбранному алгоритму функцию

    # Если пользователь выбрал постоянный шаг создаем словарь
    # С функциями вычисления постоянным шагом
    if choice_algorithm == 1:

        actions = {
            1: integral_const_step_left,
            2: integral_const_step_right,
            3: integral_const_step_trap,
            4: integral_const_step_simpson,
            5: menu
        }

    else:

        actions = {
            2: integral_double_recount_1,
            3: integral_double_recount_2
        }


    n = int(input("Введите количество разбиений: "))

    print("Вы выбрали: ", choise_method_list[choice_method],
        choice_algorithm_list[choice_algorithm],
        "количество разбиений = ", n)

    print("Введите '0', если хотите изменить данные, '1', чтобы продолжить:")

    act = int(input())

    if (act == 1 and choice_algorithm == 1):
        result = actions[choice_method](n)

    elif (act == 1 and choice_algorithm != 1):
        result = actions[choice_algorithm](n)

    elif (act == 0):
        menu()
        return

a = 1.9
b = 2.6
result = None


def integral(arg):
    return (sqrt(2 * arg + 1.7) / (2.4 + sqrt(1.2 * arg * arg + 0.6)))


def integral_const_step_left(n):

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
    return result


def integral_const_step_right(n):

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
    return result


def integral_const_step_trap(n):

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
    return result


def integral_const_step_simpson(n):

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
    return result


def integral_double_recount_1(n):

    print("Вычисляется левыми частями переменным шагом")

    global result
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

    return (I_2n)


def integral_double_recount_2(n):

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

    return I2

if __name__ == "__main__":
    menu()
