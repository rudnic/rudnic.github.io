#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n 8

int main(void) {

    double a[n] = {0.9999998, 1.0, 0.5000063, 0.1666674, 
                    0.0416350, 0.0083298, 0.0014393, 0.0002040};
    
    double e, x, u, c = a[0], p = 1.;

    printf("x = ");
    scanf("%lf", &x);
    printf("epsilon = ");
    scanf("%lf", &e);

    for (int k = 1; k < n; k++) {
        p *= x;
        u = p * a[k];
        c += u;

        if (fabs(u) <= e) {
            printf("result: %.8lf\n", c);
            return 0;
        }
    }

    printf("Требуемая точность не достигнута");

    return 0;
}

