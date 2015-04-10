#include <unistd.h>
#include <stdio.h>
void main(){
    fprintf(stderr, "-- begin -- \n");
    execl("/bin/ls", "-l", "/devops", 0);
    fprintf(stderr, "-- end -- \n");
}
