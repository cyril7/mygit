#include <stdio.h>
long recursion(int x);

long recursion(int x)
{
    if(x>1)
    {
        return x*recursion(x-1);
    }
    else if(x==1 || x==0)
    {
        return 1;
    }
    else
    {
        printf("Invalid argument!\n");
        exit(-1);
    }
}


void main(void)
{
    int num;
    long factorial;
    scanf("%d", &num);
    factorial = recursion(num);
    printf("%d!=%ld\n", num, factorial);
}
