#include<stdio.h>

int main(){

    char *canchange = "HELLO WORLD";
    puts(canchange);

    canchange = "HELLO MOTHER DUCKER ";
    puts(canchange);


    char cannotchange[] = "HELLO WORLD";
    puts(cannotchange);


    return 0;
    
    
}