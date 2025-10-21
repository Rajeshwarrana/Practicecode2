#include<stdio.h>

int main() {

	int n;
	printf("ENTER THE NUMBER OF FIBONACCIE SERIES (n>2) : ");
	scanf("%d",&n);
	
	int fib[n];
	fib[0]=0;
	fib[1]=1;	

    for(int i=2 ; i<n ; i++){
	
	    fib[n]=fib[n-1] + fib[n-2];
	    printf("%d \t" , fib[n]);

    }
}

printf("\n");
return 0;
