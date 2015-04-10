#include <stdio.h>
#include <unistd.h>
#include <signal.h>

int main() {
    pid_t pid1, pid2, pid3;
    int status;
    while (1){
        if ((pid1 = fork()) < 0) {
            exit(1);
        }
        else if(pid1 == 0) { // child proc 1
            sleep(30);
            exit(0);
        }
        if ((pid2 = fork()) < 0)  {
            exit(1);
        }
        else if(pid2 == 0) { // child proc 2
            sleep(40);
            exit(0);
        }
        // 父进程
        fprintf(stderr, "For child pid=[%d][%d].\n", pid1, pid2);
        pid3 = wait(&status); // 并发，监控子进程状态
        kill(pid1, SIGTERM); //杀死子进程1
        kill(pid2, SIGTERM); //杀死子进程2
        fprintf(stderr, "Kill childpid=[%d][%d], exit pid[%d], status[%d]\n", pid1, pid2, pid3, status);
        pid3 = wait(&status); // 两个子进程结束，所以必须wait两次
        sleep(1);
    }
    return 0;
}
