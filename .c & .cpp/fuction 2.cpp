#include <iostream>
#include <math.h>
using namespace std;

bool isprim(int num)
{
    for (int i = 2; i <= sqrt(num); i++)
    {
        if (num % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{

    int a, b;
    cin >> a >> b;

    for (int x = a; x <= b; x++)
    {
        if (isprim(x))
        {
            cout << x << endl;
        }
    }

    return 0;
}