#include <iostream>
int main() {
    // Declare variables to store two input values
    int amount1;
    int amount2;

    // Prompt the user to enter the first value
    std::cout << "Enter the first number: ";
    std::cin >> amount1; // Read the first input

    // Prompt the user to enter the second value
    std::cout << "Enter the second number: ";
    std::cin >> amount2; // Read the second input

    // Calculate the sum of the two numbers
    int sum = amount1 + amount2;

    // Print the sum
    std::cout << "The sum of " << amount1 << " and " << amount2 << " is: " << sum << std::endl;

    return 0;
}
