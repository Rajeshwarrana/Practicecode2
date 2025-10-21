#include <iostream>
using namespace std;

int trplt(int a, int b, int c)
{
    if (a > b && a > c)
    {
        if ((a * a) == ((b * b) + (c * c)))
        {
            cout << "GIVEN NUMBER IS A PYTHAGORAS TRIPLET !! " << endl;
        }
        else
        {
            cout << "GIVEN NUMBER IS NOT A PYTHAGORAS TRIPLET !! " << endl;
        }
    }

    else if (b > a && b > c)
    {
        if ((b * b) == ((a * a) + (c * c)))
        {
            cout << "GIVEN NUMBER IS A PYTHAGORAS TRIPLET !! " << endl;
        }
        else
        {
            cout << "GIVEN NUMBER IS NOT A PYTHAGORAS TRIPLET !! " << endl;
        }
    }

    else if (c > b && c > a)
    {
        if ((c * c) == ((b * b) + (a * a)))
        {
            cout << "GIVEN NUMBER IS A PYTHAGORAS TRIPLET !! " << endl;
        }
        else
        {
            cout << "GIVEN NUMBER IS NOT A PYTHAGORAS TRIPLET !! " << endl;
        }
    }
}

int main()
{
    int a, b, c;
    int x;
    cin >> a >> b >> c;

    trplt(a, b, c);

    cout << "PRESS ANY KEY TO EXIT ";
    cin >> x;

    return 0;
}