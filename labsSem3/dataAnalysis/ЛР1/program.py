n = 24

def search_accumulated_frequency(array, num):
    ''' Поиск накопленной частости элемента '''
    global n
    return search_accumulated_quantity(array, num) / n


def search_accumulated_quantity(array, num):
    ''' Поиск накопленной частоты элемента '''
    result = 0
    for i in array:
        if (i < num):
            result += 1
    return result


def search_frequency(array, num):
    ''' Поиск частости повторения элемента '''
    global n
    return search_quantity(array, num) / n


def search_quantity(array, num):
    ''' Поиск частоты повторения элемента '''
    result = 0
    for i in array:
        if i == num:
            result += 1
    return result


def main():

    source_array = [4, 0, 3, 4, 1, 0, 3, 1, 0, 4, 0, 0,
            3, 1, 0, 1, 1, 3, 2, 3, 1, 2, 1, 2]

    array = []
    for i in source_array:
        if not (i in array):
            array.append(i)

    array.sort()
    array.append(array[-1] + 1)

    print("Отсортированный массив уникальных значений")
    for i in array:
        print(i, end="\t")

    print("\nЧастоты повторения элементов:")
    for i in array:
        print(search_quantity(source_array, i), end="\t")

    print("\nЧастость повторения элементов:")
    for i in array:
        print(format(search_frequency(source_array, i), '.3f'), end="\t")

    print("\nНакопленная частота:")
    for i in array:
        print(search_accumulated_quantity(source_array, i), end="\t")

    print("\nНакопленная частость:")
    for i in array:
        print(format(search_accumulated_frequency(source_array, i), '.3f'), end="\t")

if __name__ == "__main__":
    main()
