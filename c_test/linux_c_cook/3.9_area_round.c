#include <stdio.h>

float pi=3.14f;
float area(float radius);

float area(float radius)
{
    float ret;
    ret=pi*radius*radius;
    return ret;
}

void main(void)
{
    float radius;
    float round;
    printf("Input the radius: \t");
    scanf("%f", &radius);
    round=area(radius);
    printf("The area is: %f.\n", round);
    //return;
}
