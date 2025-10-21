#include<stdio.h>

int main()
{
    int x;
    int y;
    int z;


    printf("ENTER FIRST NUMBER ");
    scanf("%d" , &x);

    printf("ENTER SECOND NUMBER ");
    scanf("%d" , &y);

    printf("ENTER WHAT YOU WANT TO DO 1 FOR ADDITION 2 FOR SUBSTRACTION ");
    scanf("%d" , &z);

    if (z==1){
        printf("ADDITION IS %d" , x+y);
    }
    if (z==2){
        print("ADDITION IS %d" , x-y);
    }

    return 0;





}