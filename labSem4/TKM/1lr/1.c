#include <stdio.h>
#include <stdlib.h>

int main() {
    float a = 0., b = 1., x0 = 0., y0 = 1., h, x = 0., y = 0.;
    int n;

    printf("Введите n: ");
    scanf("%d", &n);
    h = (b - a) / n;
    printf("h = %f\n", h);

    printf("Введите x0: ");
    scanf("%f", &x0);
    printf("Введите y0: ");
    scanf("%f", &y0);

    y = y0;

    while (x < b-h) { // x < 0.9
        y = y + h * (y * (1 - x));
        printf("x = %f\t", x);
        printf("y = %f\t\n", y);
        x = x + h;
    }

    return 0;
}