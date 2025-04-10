#include <iostream>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    long long count = 0;
    for (long long b = 1; ; ++b) {
        if(b % 2 == 0){
            continue;
        }
        long long b_squared = b * b;
        if (b_squared > n) {
            break;
        }
        for (int a = 1; ; ++a) { // a は 1 から開始
            long long power_of_2 = 1LL << a;
            long long x = power_of_2 * b_squared;
            if (x > n) {
                break;
            }
            count++;
            if (power_of_2 > n / b_squared) { // Avoid overflow
                break;
            }
        }
    }
    std::cout << count << std::endl;
    return 0;
}
