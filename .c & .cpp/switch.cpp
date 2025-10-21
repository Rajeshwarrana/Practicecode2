#include<iostream>
using namespace std;

int main(){

    char button;
    cout<<"INPUT A CHARACTER BETWEEN A AND E :-";
    cin>>button;

    switch (button){
        
        case 'a':
        cout<<"HELLO";
        break;

        case 'b':
        cout<<"NAMESTE";
        break;

        case 'c':
        cout<<"RAM RAM";
        break;

        default:
        cout<<"WORKIN ON IT !!";
        break;


    }

    return 0;
    
}