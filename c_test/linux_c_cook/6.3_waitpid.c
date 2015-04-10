#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    pid_t child_pid, pid;
    int status;
    child_pid = fork();
    switch(child_pid)
    {
        case -1:
            printf("Create Process Failed!\n");       
            break;
        case 0:
            printf("Child Process with ID: %d\n", (int)getpid());
            break;
        default:
            printf("Child Process with ID: %d, Parent Process with ID: %d\n", child_pid, (int)getpid());
            pid = wait(&status);
            printf("Child Process finished: PID=%d\n", child_pid);
            if(WIFEXITED(status))
            {
                printf("ChildProcess EXITED WITH CODE %d.\n", WEXITSTATUS(status));
            }
            else
            {
                printf("Child Process Terminated Abnormally!\n");
            }
            printf("pid var is %d.\n", pid);
            break;
    }
    return 0;
}
