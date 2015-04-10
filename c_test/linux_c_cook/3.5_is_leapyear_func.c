#include <stdio.h>

int is_leapyear(int);

int is_leapyear(int year)
{
    int ret=0;
    if (year%4==0 && year%100!=0 || (year%400==0))
    {
        ret=0;
    }
    else
    {
        ret=1;
    }
    return ret;
}

int main(void)
{
    int ret;
    int year;
    printf("Input a year you wan to know: \t");
    scanf("%d", &year);
    ret=is_leapyear(year);
    if(ret==0)
    {
        printf("%d is a leap year!\n", year);
    }
    else if(ret==1)
    {
        printf("%d is not a leap year!\n", year);
    }
    return 0;

}
