#include <stdio.h>
#include <stdlib.h>

long filesize(FILE *stream);
void main()
{
    long size, pos;
    char ch;
    FILE *fp_in, *fp_out;
    if((fp_in=fopen("ex3.9_reverse_str.txt", "r"))==NULL)
    {
        printf("can't open file !\n");
        exit(1);
    }
    if((fp_out=fopen("ex3.9_reverse_str_new.txt", "w"))==NULL)
    {
        fclose(fp_in);
        printf("cant't open file new txt.\n");
        exit(1);
    }
    pos=0;
    size=filesize(fp_in);
    while(pos++<size)
    {
        //27              putchar(ch); /* 在stdout上输出字符 */
        //(gdb) p ch
        //$1 = 10 '\n',所以 -(pos+1),从-2个字节的位置开始倒数
        fseek(fp_in, -(pos+1), SEEK_END); /* reverse order */
        ch=fgetc(fp_in); /* 从流中读取字符 */
        putchar(ch); /* 在stdout上输出字符 */
        fputc(ch, fp_out); /* 送一个字符到一个流中  */
    }
    fclose(fp_in);
    fclose(fp_out);
}

long filesize(FILE *stream)
{
    int curpos, length;
    curpos = ftell(stream);  /* 指针定位到文件初始位置 */
    fseek(stream, 0L, SEEK_END); /* 文件指针移动到文件末尾 */
    length = ftell(stream); /* 获取已经到末尾的指针位置 */
    fseek(stream, curpos, SEEK_SET); /* 文件指针重新移动到文件头部*/
    return length;
}
