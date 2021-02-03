#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Использующиеся константы компилятора GCC:
M_PI - число Пи
M_PI_2 - Пи / 2
M_PI_4 - Пи / 4 */

#define a 0.0d
#define b M_PI_2
#define c 0.0d
#define d M_PI_4

int main(void) {

    int nx, ny;
    double hx, hy, x, y;
    double sx = 0.0, sy = 0.0, ix = 0.0, iy = 0.0; 

    printf("nx = ");
    scanf("%d", &nx);

    printf("ny = ");
    scanf("%d", &ny);

    hx = (b - a) / nx;
    hy = (d - c) / ny;
    printf("hx = %lf\n", hx);
    printf("hy = %lf\n", hy);

    x = a;

    while (x <= (b - hx)) {

        y = c;
        sy = 0;

        while (y <= (d - hy)) {
            sy += fabs(sin(x+y));
            y += hy;
        }

        iy = hy * sy;
        sx += iy;
        x += hx;
    }

    ix = hx * sx;

    printf("Result: %lf", ix);

    return 0;
}



