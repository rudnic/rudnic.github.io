#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// ОДЗ: x > 2
// Так как а < ОДЗ, начало отрезка будем считать за 2 + e

double function(double arg) {
    return ( pow((arg - 3), 2) * (-log2(arg-2)) + 1 );
}

int main(void) {

    double a, b, e, x0, x, R;

    printf("Введите точность:");
    scanf("%lf", &e);

    a = 2 + e;
    b = 10;

    x0 = a - (function(a) * (b - a)) / (function(b) - function(a));;
    R = 1;

    int k = 0;

    while ( R > e ) {

        if (function(x0) * function(b) < 0)
            x = x0 - function(x0) / (function(b) - function(x0)) * (b - x0);
        if (function(x0) * function(a) < 0)
            x = x0 - function(x0) / (function(x0) - function(a)) * (x0 - a);
        R = fabs(x - x0);
        x0 = x;
        k += 1;
    }

    printf("%lf", x);
    printf("\n%d", k);

    return 0;
}


