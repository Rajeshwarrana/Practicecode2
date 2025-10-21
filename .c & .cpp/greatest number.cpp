#include<iostream>
using namespace std;


int main(){
    
    int a , b , c ;

    cout<<"ENTER THREE NUMBERS :- ";

    cin>>a>>b>>c;

    if(a>b && a>c){

        cout<<"BIGGEST NUMBER IS :-"<<a;

    }

    else if(b>a && b>c){

        cout<<"BIGGEST NUMBER IS :-"<<b;

    }

    else{

        cout<<"BIGGEST NUMBER IS :-"<<c;
        
    }
}



