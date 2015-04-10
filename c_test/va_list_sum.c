#include <stdarg.h>
int mysum(int i, ...)
{
    int r=0, j=0;
    va_list pvar;
    va_start(pvar, i);
    for(j=0; j<i; ++j)
    {
        r += va_arg(pvar, int);
    }
    va_end(pvar);
    return(r);
}

void main(void)
{
    printf("sum(1,4)=%d\n",mysum(1,4));  
    printf("sum(2,4,8)=%d\n",mysum(2,4,8));  
}
