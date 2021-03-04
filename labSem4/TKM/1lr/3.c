#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    float a = 0, b = 0.3;
    float x = 2, y = 1, z = 1;
    float h;
    int n;

    printf("Введите n: ");
    scanf("%d", &n);
    h = (b - a) / n;
    printf("h = %f\n", h);

    float i = a;

    while (i < b-h) {
        x = x + h * (-2 * x + 5 * z);
        y = y + h * (sinf(i-1) * x - y + 3 * z);
        z = z + h * (-x + 2 * z);
        printf("x = %f,\t y = %f,\t z = %f,\t i = %f\t\n", x, y, z, i);

        i += h;
    }

    return 0;
}