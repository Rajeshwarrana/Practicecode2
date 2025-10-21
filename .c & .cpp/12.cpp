#include<iostream>
using namespace std;

int main(){
    long long a;
    cout << "ENTER NUMBER: ";
    cin >> a;

    if(a % 2 == 0){
        cout << "EVEN NUMBER";
    }
    else{
        cout << "ODD NUMBER";
    }

    return 0;
}
