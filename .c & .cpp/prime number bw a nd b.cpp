#include<iostream>
using namespace std;

int main(){
    int a , b;
    int i;
    int num;
    cout<<"ENTER NUMBERS 1 ";
    cin>>a;
    cout<<"ENTER NUMBER 2 ";
    cin>>b;
    

    for(num=a ; num<=b ; num++ ){
        for(i=2 ; i<num ; i++){
            if(num%i==0){
                break;

            }
        }
        if(i==num){
            cout<<num<<endl;      
        }        
    }
    

    return 0;
}