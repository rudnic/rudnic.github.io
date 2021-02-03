#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// ОДЗ: x > 2
// Так как а < ОДЗ, начало отрезка будем считать за 2 + e

double function(double arg) {
    return ( pow((arg - 3), 2) * (-log2(arg-2)) + 1 );
}

double division_segment(double segment_start, double segment_end, double eps) {
    
    /* Идея функции заключается в том, что подаются начало и конец отрезка и точность
       Вычисляется середина переданного отрезка, и если функция имеет разные знаки на отрезке
       [segment_start, x] и длина отрезка больше заданной точности, то функция вызывает саму себя уже 
       с ноыми значениями, где начало отрезка будет такое же, а конец - середина предыдущего отрезка
       аналогично, для ситуации, если f(segment_start) * f(x) > 0, а f(x) * f(segment_end) < 0
       таким образом получается рекурсивная функция */

    double x = (segment_start + segment_end) / 2;

    if ( (function(segment_start) * function(x)) < 0) {
        if ( fabs(x - segment_start) <= eps )
            return x;
        return division_segment(segment_start, x, eps);
    }

    if ( (function(x) * function(segment_end)) < 0) {
        if ( fabs(segment_end - x) <= eps )
            return x;
        return division_segment(x, segment_end, eps);
    }

    /* Если функция дошла до этой части, тогда функция равна нулю будет 
       в одной из трёх точек: segment_start, segment_end, x
       поэтому проверяем в каком из этих точек функция обращается в 0 */
       
    if ( function(segment_start) == 0 )
        return segment_start;
    else if ( function(segment_end) == 0 )
        return segment_end;
    else 
        return x;

}

int main(void) {

    double a, b, e, res;

    printf("Введите точность:");
    scanf("%lf", &e);

    a = 2 + e;
    b = 10;

    res = division_segment(a, b, e);
    printf("%lf", res);

    return 0;
}


