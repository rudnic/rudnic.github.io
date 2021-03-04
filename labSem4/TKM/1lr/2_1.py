def main():
    r = 0.03
    T = 83
    Ts = 22
    n = int(input("Введите количество разбиений: "))
    h = (Ts - T) / n
    t = 0

    while T > Ts:
        t += h * (-r * (T - Ts))
        T += h
        print(round(t, 4), end="\t\t")
        print(round(T, 4))

if __name__ == "__main__":
    main()