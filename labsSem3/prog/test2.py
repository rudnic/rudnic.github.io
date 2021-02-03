# Решение Рудницкого Никиты
# Этот алгоритм эффективен по памяти, потому что не используюся сложные структуры данных
# И по времени, потому что сложность алгоритма равна O(n * log(n))

def two_sum_hashed(lst, target):
    # Исходный массив сортируется встроенной функцией языка Python
    # Её сложность в лучшем случае оценивается O(n)
    # И в среднем и худших случаях O(n * log(n))
    # Используется алгоритм сортировки Timsort
    # Подробнее: https://habr.com/ru/company/infopulse/blog/133303/

    lst.sort()

    # Основная идея алгоритма поиска пар чисел заключается в следующем
    # Берутся два индекса - нулевой (первый элемент) и индекс последнего элемента
    # В цикле сравнивается сумма элементов по этим индесам и если она равна заданному числу
    # Выводятся индексы этих чисел и сами числа
    # Если их сумма больше заданного числа, second уменьшается на 1
    # И сравниваются уже первое и предпоследнее число
    # Если их сумма меньше, firt увеличивается на 1 и сравнивается уже второе число
    # Цикл выполняется до тех пор, пока second > first
    # Таким образом в отсортированном массиве будут сравниваться пары чисел
    # И выводиться индексы из ОТСОРТИРОВАННОГО массива
    # Сложность такого алгоритма в худшем случае будет равняться O(n)
    first = 0
    second = len(lst) - 1
    result = []
    pair = ()
    print("Отсортированный массив:")
    print(lst)
    while first < second:
        if (lst[first] + lst[second]) == target:
            pair = (first, second)
            result.append(pair)
            print("Индексы: " + str(first) + "; " + str(second), "Значения: ", lst[first], lst[second])
            first += 1
            second -= 1
        elif (first + second) < target:
            first += 1
        else:
            second -= 1
        
    return result

# Общая сложность алгоритма: O(n*log(n) + n) = O(n*log(n)) = O(n)

if __name__ == "__main__":

    print(two_sum_hashed([1, 0, 0, 1, 1], 0))