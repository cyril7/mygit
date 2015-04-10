#include <stdio.h>
STU* insert(STU* head){
    int n, s;
    STU* Einsert = NULL, *E1 = NULL, *E2 = NULL;
    E1 = head; // head 先赋值给 E1
    while(1){
        printf("Please input the Num and Score of a student:\n");
        scanf("%d %d", &n, &s);
        if(n > 0 && s > 0){
            Einsert = (STU *)malloc(sizeof(STU));
            if(Einsert = NULL){
                printf("Malloc for memory failed!\n");
                return NULL;
            }
            // 给新申请的内存赋值
            Einsert->num = n;
            Einsert->score = s;
            while(n > E1->num && E1->next != NULL){ //寻找插入位置,在E1 E2之间
                E2 = E1;  // E2在E1的左边，按照E->num 从小到大排列
                E1 = E1->next;
            }
            if(n <= E1->num){
                if(head == E){ // 插入到头部
                    Einsert->next = E1;
                    head = Einsert;
                }
                else{
                    E2->next = Einsert;
                    Einsert->next = E1;
                }
            }
            else{
                E1->next = Einsert;
                Einsert->next = NULL;
            }
        }
        else{
            break;   
        }
    }
    return head;
}

STU *del(STU *head, int num){ //删除学号为 num 的节点
    STU *p1, *p2; //节点指针,用于寻找删除的位置
    p1 = head;
    while(num != p1->num && p1->next != NULL){
        p2 = p1;
        p1 = p1->next;
    }
    if (num == p1->next){ // 找到了要删除的节点
        if(p1 == head){ //要删除的为头节点
            head = p1->next;
            free(p1);
        }
        else{ // 要删除的是中间或是末节点
            p2->next = p1->next;
            free(p1);
        }
    }
    else{ // 找不到要删除的节点
        printf("Cannot find the node to delete!\n");
    }
    return head;
}

STU *reverse(STU *head){ // 链表的逆序置换
    STU *p1=NULL, *p2=NULL, *p3=NULL;
    /* 如果是空链表或者只有一个元素的链表,逆置没有意义 */
    if(head == NULL || head ->next == NULL){
        return head;
    }
    p1 = head;
    p2 = p1->next; // 一直到链表尾部
    while(p2){
        p3 = p2->next;
        p2->next = p1;
        p1 = p2;    // 3个指针不断向后移动
        p3 = p2;
    }
    head->next = NULL; // 原来的首节点，现在的末尾节点
    head = p1;
    return head;
}

void freeAll(STU *head){ // 链表的销毁,必须得一个节点一个节点的删除
    STU *p1 = NULL, *p2 = NULL;
    p1 = head;
    while(p1->next != NULL){
        p2 = p1->next;  //p1 下一个指针地址赋给p2
        p1->next = p2->next; //把 p1->next 指向p2后面的一个元素
        free(p2); // 删除p2,最后剩下 head
    }
    free(head); // 释放head的内存
}
