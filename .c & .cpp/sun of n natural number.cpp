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

    int n;
    cin >> n;

    sumn(n);

    return 0;
}