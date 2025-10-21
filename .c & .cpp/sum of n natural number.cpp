#include <iostream>
using namespace std;

int sumn(int n)
{
    int add = 0;
    for (int i = 1; i <= n; i++)
    {
        add += i;
    }
    cout<<"SUM OF NATURAL NUMBER TILL GIVEN IS :- "<<add;
    return add;
}

int main()
{

    int n,x;
    cin >> n;

    sumn(n);

    cout << "PRESS ANY KEY TO EXIT ";
    cin >> x;


    return 0;
}