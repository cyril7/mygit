#include <stdio.h>

void swapvalues(int *x_ptr, int *y_ptr);


void swapvalues(int *x_ptr, int *y_ptr)
{
    int temp=*x_ptr;
    if(*x_ptr < *y_ptr)
    {
        *x_ptr=*y_ptr;
        *y_ptr=temp;
    } 
}

void main()
{
    int a, b;
    int *a_ptr, *b_ptr;
    a_ptr=&a;
    b_ptr=&b;
    printf("Input two numbers a b: \t");
    scanf("%d %d", a_ptr, b_ptr);
    swapvalues(a_ptr, b_ptr);
    printf("a=%d, b=%d\n", *a_ptr, *b_ptr);
}
