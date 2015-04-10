#include <unistd.h>
#include <stdio.h>
void main(){
    int fildes[2];
    pid_t pid;
    int j;
    char buf[256];
    // 父进程创建管道，返回无名管道的两个文件描述符 fildes[0] fildes[1]
    if (pipe(fildes) < 0){
        fprintf(stderr, "pip error!\n");
        return;
    }
    if ((pid = fork()) < 0 ){
        fprintf(stderr, "for error!\n");
        return;
    }
    if (pid == 0) { // 子进程
        close(fildes[1]); // 子进程关闭向管道输入，只读管道
        memset(buf, 0, sizeof(buf));
        j = read(fildes[0], buf, sizeof(buf)); // 读管道
        fprintf(stderr, "[child] buf=[ %s ] len[ %d]\n", buf, j);
        return;
    }
    // 此时为父进程,关闭从管道输出，只写管道
    close(fildes[0]);
    write(fildes[1], "hello!", strlen("hello!"));
    write(fildes[1], "world!", strlen("world!"));
}
