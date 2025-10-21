#include<iostream>
using namespace std;

int main() {
    int n;
    cout << "ENTER NUMBER: ";
    cin >> n;

    if (n <= 1) {
        cout << "NON PRIME NUMBER";
        return 0;
    }

    bool isPrime = true;
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime) {
        cout << "PRIME NUMBER";
    } else {
        cout << "NON PRIME NUMBER";
    }

    return 0;
}
