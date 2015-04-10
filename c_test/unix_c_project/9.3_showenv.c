#include <stdio.h>
extern char **environ;
void main(){
    char **p = environ;
    while (*p){
        // environ 数组的首地址 = *p
        fprintf(stderr, "%s.\n", *p);
        p++;
    }
}
