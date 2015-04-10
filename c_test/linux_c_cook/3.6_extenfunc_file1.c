#include <stdio.h>
//#include <3.6_extenfunc_file2.c>
#include "3.6_extenfunc_file2.c"
/* file1.c */
extern int max(int x, int y);
void main(void)
{
    int c, a=20, b=8;
    c=max(a, b);
    printf("c is %d\n", c);
}
