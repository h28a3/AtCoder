#include <iostream>
using namespace std;

// 階乗を計算する関数
unsigned long long factorial(int n) {
    unsigned long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
        if (result > 3000000000000000000ULL) break; // オーバーフローを防ぐ
    }
    return result;
}

int main() {
    unsigned long long X;
    cin >> X;

    int N = 1;
    unsigned long long fact = 1;

    // N! が X に達するまで計算
    while (fact < X) {
        N++;
        fact = factorial(N);
    }

    // 答えを出力
    if (fact == X) {
        cout << N << endl;
    } else {
        cout << "Error: No valid N found." << endl; // 制約上、このケースは起きないはず
    }

    return 0;
}
