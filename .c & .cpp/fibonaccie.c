#include<stdio.h>

void printname(char arr[]);

int main(){

    char firstname[] = "Rajeshwar";
    char lastname[] = "Rana";

    printname(firstname);
    printname(lastname);

    return 0;


}

void printname(char arr[]){
    for(int i=0 ; arr[i] != '\0'; i++) {
        printf("%c",arr[i]);
    }

    printf("/n");
}
