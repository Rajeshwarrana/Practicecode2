#include<iostream>
using namespace std;

int main(){

    int a;
    cin>>a;

    if(a%2==0 && a%3==0){
        cout<<a<<"  IS DIVISIBLE BY BOTH 2 AND 3";
    }

    else if(a%2==0){
        cout<<a<<" IS DIVISIBLE ONLY BY 2 ";

    }

    else if(a%3==0){
        cout<<a<<" IS DIVISIBLE ONLY BY 3 ";

    }
    
    return 0;
    
}   