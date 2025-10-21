#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "ENTER THE NUMBER YOU WANT IN REVERSE :- ";
    cin >> n;

    int reverse = 0;

    while (n > 0)
    {
        int lst = n % 10;

        reverse = reverse * 10 + lst;
        n = n / 10;
    }
    cout << "THE REVERSE OF THE NUMBER IS :- ";
    cout << reverse << endl;
}