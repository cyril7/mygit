#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("Current Process ID: %d\n", (int) getpid());
    printf("Parent Process ID: %d\n", (int) getppid());
    return 0;
}

