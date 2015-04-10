void main(void)
{
    int a=2;
    int b=3;
    //if
    if(a>b)
    {
        a++;
    }
    else
    {
        b++;
    }
    printf("a: %d, b: %d.\n", a, b);
    //switch
    char c='d';
    switch(c)
    {
        case 'd':
            printf("c=d.\n");
        break;
        case 'e':
            printf("c=e.\n");
        break;
        default:
            printf("Unknown!\n");
        break;
    }
    //while
    int i=0;
    while(++i<3)
    {
        printf("Value i is: %d\n", i);
    }
    //do ... while
    int j=0;
    do {
        printf("j = %d.\n",j);
    }while(++j<3);
    //for
    int k=0;
    for(k=0;k<3;k++)
    {
        printf("k = %d\n", k);
    }
}
