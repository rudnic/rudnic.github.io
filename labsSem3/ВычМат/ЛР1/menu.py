from math import *
#from integral import *
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


if __name__ == "__main__":
    menu()
