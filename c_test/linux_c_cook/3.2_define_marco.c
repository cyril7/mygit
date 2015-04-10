#include <stdio.h>

#define M (x*y+z)
#define SQUARE(x) x*x
void main(void)
{
    int sum=0;
    int x=2, y=3, z=4;
    sum = M+9*M+M*M;
    printf("sum= %d\n", sum);

    int s=0;
    s = SQUARE(9);
    printf("s= %d\n", s);
}
