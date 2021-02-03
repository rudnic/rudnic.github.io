#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 5

int main(void) {

    double a[n] = {1.000000002, -0.166666589, 0.008333075, 
                    -0.000198107, 0.000002608};
    
    double e, x, u, c, p = 1.;

    printf("Введите x в градусах:\n");
    printf("x = ");
    scanf("%lf", &x);

    x = M_PI * x / 180;
    c = a[0] * x;
    
    printf("epsilon = ");
    scanf("%lf", &e);

    for (int k = 1; k < n; k++) {
        p *= (x * x);
        u = p * a[k] * x;
        c += u;

        if (fabs(u) <= e) {
            printf("result: %.8lf\n", c);
            return 0;
        }
    }

    printf("Требуемая точность не достигнута");

    return 0;
}

