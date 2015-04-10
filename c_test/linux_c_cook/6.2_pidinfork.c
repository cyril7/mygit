#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    pid_t child_pid;
    child_pid = fork();
    // 若子进程创建失败， fork()返回-1
    // 若子进程创建成功, fork()函数在子进程中返回0，在父进程中返回子进程ID
    switch(child_pid)
    {
        case -1:
            printf("Create Process Failed!\n");
            break;
        case 0:
            printf("Child Process with ID %d.\n", (int)getpid());
            break;
        default:
            printf("Parent Process with ID %d, Child Process with ID %d.\n", (int)getpid(), (int)child_pid);
            break;
    }
    return 0;
}
