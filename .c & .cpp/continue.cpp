#include<iostream>
using namespace std;

int main(){
    
    for(int num=1 ; num<=100 ; num++){
        if(num%3==0){
            cout<<"-";
            continue; 
        }
        cout<<num<<" ";

    }

    return 0;
    
}