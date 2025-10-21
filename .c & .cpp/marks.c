#include <stdio.h>

int main()
{
    int n;
    printf("ENTER OUR OVER ALL MARKS :- ");
    scanf("%d", &n);

    if (n < 30)
    {
        printf("C grade !! ");
    }
    else if (n >= 30 && n < 70)
    {
        printf("B grade !! ");
    }

    else if (n >= 70 && n < 90)
    {
        printf("A grade !! ");
    }
    else if (n >= 90 && n <= 100)
    {
        printf("A+ grade !! ");
    }
    else
    {
        printf("ENTER CORRECT MARKS ");
    }

    return 0;
    
}