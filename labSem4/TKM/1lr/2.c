#include <stdio.h>
#include <stdlib.h>

int main() {
    float a = 1., b = 1.5, x0 = 0., h, x, y = 0.77, z = -0.44;
    int n;

    printf("Введите n: ");
    scanf("%d", &n);
    h = (b - a) / n;
    printf("h = %f\n", h);

    x = a;
    while (x < b-h) {
        y = y + h * z;
        z = z - h * (z / x + y);
        printf("x = %f\t", x);
        printf("y = %f\t", y);
        printf("z = %f\n", z);
        x = x + h;
    }
    
    return 0;
}