#include <signal.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/time.h>

void signalhandle(int signal)
{
    switch(signal)
    {
        case SIGHUP:
            printf("Catch Signal: SIGHUP (%d)\n", signal);
            break;
        case SIGINT:
            printf("Catch Signal:SIGINT (%d)\n", signal);
            break;
        case SIGQUIT:
            printf("Catch Signal:SIGQUIT (%d)\n", signal);
            break;
        case SIGALRM:
            printf("Catch Signal:SIGALARM (%d)\n", signal);
            break;
        default:
            printf("Unkown Signal: %d", signal);
            break;
    }
}

int main()
{
    int sec_delay=5;
    printf("Current Process ID: %d\n", (int)getpid());
    signal(SIGINT, signalhandle);
    signal(SIGQUIT, signalhandle);
    signal(SIGALRM, signalhandle);
    alarm(sec_delay);
    while(1)
    {
        pause();
    }
    return 0;
}
