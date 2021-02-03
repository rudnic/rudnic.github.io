# include <stdio.h>
# include <math.h>
 float RLF(float p)
 {
    float E=powf(10,-6);
    float d=1;
    float u=6;
    float hv;
    float hd;
    float hs;
    float R;
    float s;
    float I1=0;
    float I2=0;
    hv=(u-d)/p;
    hd=hv;
    hs=d;
    tp:
    s=0;
    float x=hs;
    while (x<=(u-hv))
    {
        s+=sqrt(x*x*x+14)/(x*x*3)-5*x;
        x+=hd;
    }
    I2=hd*s;
    R=abs(I2-I1);
    I1=I2;
    if(hd==hv)
    {
    hd=hv/2;
    hv=hv/4;
    }
    else{
    hd=hv;
    hs=hd/2;
    hv=hv/2;}
    if (R>E)
    {
        goto tp;
    }
    return I2;
 }
i=RLF(5);
printf(i,%f);


a = 1.9
b = 2.6
result = None
