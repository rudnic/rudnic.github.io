def main():
    n = int(input("Введите количество разбиений: "))
    a = 0.0
    b = 1.0
    x = a
    y = 1
    h = (b - a) / n

    while (x < b - h):
        y += h * (y * (1 - x))
        print("x = ", round(x, 4), end="\t")
        print("y = ", round(y, 4))
        x += h

if __name__ == "__main__":
    main()