def gen_bin_tree(height, root):

    bin_tree = {}

    # hashing = lambda a: hash((a, time.time)) #хэш функция
    left_child_func = lambda a: a + 6 # функция вычисления левого потомка
    right_child_func = lambda a: a + 1 # функция вычисления правого потомка

    left_child = left_child_func(root)
    right_child = right_child_func(root)
    bin_tree[root] = [None, left_child, right_child]

    i = 1
    parent = root
    while i < height:
        bin_tree[left_child] = [parent, left_child_func(left_child), right_child_func(left_child)]
        parent = left_child
        left_child = left_child_func(parent)
        right_child = right_child_func(parent)
        i += 1

    i = 1
    parent = root
    left_child = left_child_func(root)
    right_child = right_child_func(root)
    while i < height:
        bin_tree[right_child] = [parent, left_child_func(right_child), right_child_func(right_child)]
        parent = right_child
        left_child = left_child_func(parent)
        right_child = right_child_func(parent)
        i += 1

    for i in bin_tree.values():
        i.pop(0)

    print(bin_tree)
    # print_bin_tree(bin_tree)


def main():
    gen_bin_tree(5, 3)

if __name__ == "__main__":
    main()


