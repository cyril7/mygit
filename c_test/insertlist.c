#include <stdio.h>
STU* insert(STU* head){
    int n, s;
    STU* Einsert = NULL, *E1 = NULL, *E2 = NULL;
    E1 = head;
    while(1){
        printf("Please input the Num and Score of a student:\n");
        scanf("%d %d", &n, &s);
        if(n > 0 && s > 0){
            Einsert = (STU *)malloc(sizeof(STU));
            if(Einsert = NULL){
                printf("Malloc for memory failed!\n");
                return NULL;
            }
            Einsert->num = n;
            Einsert->score = s;
            while(n > E1->num && E1->next != NULL){

            }
        }
        else{
            break;   
        }
    }
}
