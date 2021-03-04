
def main():
    n = int(input("Введите количество разбиений: "))
    a = 1.0
    b = 1.5
    x = a
    h = (b - a) / n
    y = 0.77
    z = -0.44

    while (x < b - h):
        y += h * z
        z -= h * (z / x + y)
        print("x = ", round(x, 4), end = "\t")
        print("y = ", round(y, 4), end = "\t")
        print("z = ", round(z, 4))
        x += h

    return

if __name__ == "__main__":
    main()