#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

    double e, y0 = 1.5, y, x = 0.464, R = 1;

    printf("epsilon = ");
    scanf("%lf", &e);

    printf("При x = %lf, y0 = %lf, eps = %lf\n", x, y0, e);

    while ( R > e ) {

        y = y0 / 2 * (3 - x * y0 * y0);
        R = fabs(y - y0);
        y0 = y;

    }
    
    printf("Результат вычисления: %lf\n", y);

    return 0;
}

    