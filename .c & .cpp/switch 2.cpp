#include <iostream>
using namespace std;

int main()
{
    char v = 'x'; // 'v' should be of type char, initialized to 'x'

    while (v == 'x')
    {
        int a1;
        int a2;
        char a;

        cout << "ENTER NUMBER 1: ";
        cin >> a1;
        cout << "ENTER NUMBER 2: ";
        cin >> a2;
        cout << "ENTER OPERATION (a: addition, b: subtraction, c: multiplication, d: division): ";
        cin >> a;

        switch (a)
        {
        case 'a':
        {
            int x = a1 + a2;
            cout << "ADDITION OF BOTH NUMBERS IS: " << x << endl;
            break;
        }
        case 'b':
        {
            int y = a1 - a2;
            cout << "SUBTRACTION OF BOTH NUMBERS IS: " << y << endl;
            break;
        }
        case 'c':
        {
            int z = a1 * a2;
            cout << "MULTIPLICATION OF BOTH NUMBERS IS: " << z << endl;
            break;
        }
        case 'd':
        {
            if (a2 == 0)
            {
                cout << "DIVISION BY ZERO IS NOT ALLOWED!" << endl;
            }
            else
            {
                double n = static_cast<double>(a1) / a2;
                cout << "DIVISION OF BOTH NUMBERS IS: " << n << endl;
            }
            break;
        }
        default:
        {
            cout << "CHOOSE CORRECT OPTION!!" << endl;
            break;
        }
        }

        cout << "Press 'x' to continue or any other key to exit: ";
        cin >> v;
    }

    return 0;
}
