#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int sum = 0;
    int orgn = n;

    while (n > 0) {
        int lst = n % 10;
        sum += lst * lst * lst;
        n = n / 10;
    }

    cout << "Sum of cubes: " << sum << endl;  // Debug statement to check the sum
    cout << "Original number: " << orgn << endl;  // Debug statement to check the original number

    if (sum == orgn) {
        cout << "ARMSTRONG NUMBER";
    } else {
        cout << "NOT AN ARMSTRONG NUMBER";
    }

    return 0;
}

