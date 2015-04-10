#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
void main(){
    char cmd[] = {"/bin/ls -l /devops"};
    system(cmd);
}
