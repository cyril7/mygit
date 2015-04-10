#include <stdio.h>

void main()
{
    char ch;
    FILE *fp;
    fp =fopen("/etc/inittab", "r");
    while((ch=fgetc(fp))!=EOF)
    {
        putchar(ch);
    }
    
}
