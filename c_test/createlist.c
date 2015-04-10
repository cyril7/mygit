#include <stdio.h>
//#include <conio.h>

struct student
{
    int num;
    int score;
    struct student *next;
};
typedef struct student STU;
STU *create(void)
{
    STU *head=NULL;
    STU *tail=NULL;
    head=(STU *)malloc(sizeof(STU));
    if(head == NULL)
    {
        printf("Head node malloc failed!\n");
        return NULL;
    }
    head->next=NULL;
    tail=head;
    STU *pNewElement=NULL;
    int n,s;
    while(1)
    {
        printf("Please input the num and score of a student: \n");
        scanf("%d %d", &n, &s);
        if(n>0 && s>0)
        {
            pNewElement=(STU *)malloc(sizeof(STU));
            if(pNewElement==NULL)
            {
                printf("Node pNewElement malloc failed!\n");
                return NULL;
            }  
            pNewElement->num=n;
            pNewElement->score=s;
            tail->next=pNewElement; /* 指针域指向pNewElement */
            tail=pNewElement; /* tail节点指向pNewElement */
        }
        else
        {
            break;
        }
    }
    pNewElement=head; /* pNewElement置为NULL */
    head=head->next; /* 移动head指针指向第一个元素 */
    free(pNewElement);
    return head;
}

void disp(STU *head)
{
    STU *p=head;
    while(1)
    {
        if(p==NULL) return ;
        printf("(Num: %d, Score: %d)\n", p->num, p->score);
        p=p->next;
    }
}

void main(void)
{
    STU *head=NULL;
    head=create();
    disp(head);
    printf("haha all done!\n");
    return ;
}
