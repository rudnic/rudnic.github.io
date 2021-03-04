def main():
    R = 50
    E = 300
    L = 30
    h = float(input("Введите шаг: "))
    I = 0
    t = 0

    while (I < 1):
        t += h * (L / (E - R * I))
        I += h
        print(round(t, 4), end="\t\t")
        print(round(I, 4))

if __name__ == "__main__":
    main()