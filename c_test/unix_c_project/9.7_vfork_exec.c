#include <unistd.h>
#include <stdio.h>
void main(){
    pid_t pid;
    if ((pid = vfork()) == 0 ) {  // 子进程
        fprintf(stderr, "-- begin in Child pid [ %d ] --\n", getpid());
        execl("/bin/ls", "-l", "/devops", 0, NULL );
        fprintf(stderr, "-- end --\n"); // will never be executed
    }
    else if( pid > 0 ) { // 父进程
        fprintf(stderr, "Parent pid = [ %d ], Chile pid = [ %d ]\n", getpid(), pid);
    }
    else {
        fprintf(stderr, "Fork failed.\n"); // fork 失败
    }
}
