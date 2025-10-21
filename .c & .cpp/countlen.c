#include<stdio.h>

int countlen(char arr[]);


int main(){

    char name[100];
    printf("ENTER YOUR FIRST NAME : ");
    fgets(name , 100 , stdin);

    printf("lenght is : %d" , countlen(name));

    return 0;

}

int countlen(char arr[]){
    int count = 0;
    for (int i=0 ; arr[i] != '\0' ; i++ ){
        count++;
    }

    return count-1;
}

