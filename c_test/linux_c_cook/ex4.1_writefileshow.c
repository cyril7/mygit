#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define SIZE 100
int main()
{
    int size;
    char strin[SIZE], strout[SIZE]; // 声明一个字符数组，用来存放输入的数据
    FILE *stream;
    if((stream=fopen("ex4.1_writefileshow.data", "w+"))==NULL)
    {
        printf("can't open file !\n");
        exit(1);
    }
    fgets(strin, SIZE, stdin); // 由键盘输入数据
    fwrite(strin, sizeof(char), SIZE, stream);
    rewind(stream); //stream重新指向文件ex4.1_writefileshow.data的开始位置
    size=fread(strout, sizeof(char), SIZE, stream);
    printf("%s", strout);
    fclose(stream);
    return 0;
}
