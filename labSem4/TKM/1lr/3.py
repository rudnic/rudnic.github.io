from math import sin

def main():
    n = int(input("Введите количество разбиений: "))
    a = 0
    b = 0.3
    x = 2
    y = 1
    z = 1
    h = (b - a) / n
    t = a

    while (t < b-h):
        x = x + h * (-2 * x + 5 * z)
        y = y + h * (sin(t-1) * x - y + 3 * z)
        z = z + h * (-x + 2 * z)
        print("x = ", round(x, 4), end="\t")
        print("y = ", round(y, 4), end="\t")
        print("z = ", round(z, 4), end="\t")
        print("t = ", round(t, 4))

        t += h

if __name__ == "__main__":
    main()