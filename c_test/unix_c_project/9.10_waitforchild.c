#include <unistd.h>
#include <stdio.h>

void main(){
    pid_t i, j;
    int status;
    if ( (i = fork()) == 0){ // 子进程
        fprintf(stderr, "child begin. pid=[%d].\n", getpid());
        sleep(5);
        fprintf(stderr, "child end. pid=[%d].\n", getpid());
        exit(10);
    }
    //父进程
    j = wait(&status);
    fprintf(stderr, "child pid=[%d], exit pid[%d], stats[%d].\n", i, j, status);
}
