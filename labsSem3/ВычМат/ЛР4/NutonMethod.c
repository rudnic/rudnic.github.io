#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// ОДЗ: x > 2

double function(double arg) {
    return ( pow((arg - 3), 2) * (-log2(arg-2)) + 1 );
}

double derivative(double arg) {
    return ( -2 * (arg - 3) * log2(arg - 2) - (arg - 3) * (arg - 3) / (arg * log(2)) );
}

int main(void) {

    double e, x, x1, r;

    printf("Введите точность: ");
    scanf("%lf", &e);
    
    int k = 0;

    x = 10;

    do {
        x1 = x - function(x) / derivative(x);
        r = fabs(x - x1);
        x = x1;
        k += 1;
    } while (r > e);

    printf("Result: %lf\n", x);
    printf("Количество итераций: %d", k);
    return 0;
}

