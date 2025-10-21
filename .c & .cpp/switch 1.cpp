#include<iostream>
using namespace std;

int main(){


    int a1;
    int a2;
    char a;


    cout<<"ENTER NUMBER 1:- ";
    cin>>a1;
    cout<<"ENTER NUMBER 2:-";
    cin>>a2;
    cout<<"ENTER   a:-addition    b:-substraction    c:-multiplication     d:-division      :-    ";

    cin>>a;

    switch(a){

        case 'a':
        int x=a1+a2;
        cout<<"ADITTION OF BOTH NUMBER IS :-    "<<x;
        break;

        case 'b':
        int y=a1-a2;  
        cout<<"SUBSTRACTIO OF BOTH NUMBERS IS :-   "<<y;
        break;

        case 'c':
        int z=a1*a2;
        cout<<"MULTIPLICATION OF BOTH NUMBER IS :-   "<<z;
        break;
        
        case 'd':
        int n=a1/a2;
        cout<<"DIVISION OF BOTH NUMBERS IS :-   "<<n;
        break;

        default:
        cout<<"CHOOSE CORRECT OPTION !!";
        break;






    }

    return 0;
    

}