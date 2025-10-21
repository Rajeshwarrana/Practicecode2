#include <stdio.h>

int main()
{

    int n;
    printf("ENTER NUMBER WHOSE TABLE YOU WANT := ");
    scanf("%d", &n);

    for (int i = 1; i <= 10; i++)
    {
        printf("%d \n", n * i);
    }

    return 0;
}