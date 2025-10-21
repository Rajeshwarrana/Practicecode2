#include<stdio.h>

int main(){

    char firstname[30];
    char lastname[20];

    printf("ENTER YOUR FIRST AND LAST NAME  :- ");
    scanf("%s",firstname);
    scanf("%s",lastname);

    printf("YOUR FULL NAME IS %s %s\n",firstname , lastname );
    printf("\n");

    return 0;
    
}