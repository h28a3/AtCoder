#include <iostream>
#include <vector>
#include <unordered_map>
#include <iomanip>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<vector<int>> dice(N);
    vector<int> K(N);
    vector<double> probability(N);

    // 入力の処理と総面数の計算
    for (int i = 0; i < N; ++i) {
        cin >> K[i];
        dice[i].resize(K[i]);
        for (int j = 0; j < K[i]; ++j) {
            cin >> dice[i][j];
        }
    }

    double maxProbability = 0.0;

    // 2つのサイコロの組み合わせを試す
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            unordered_map<int, double> freq_i, freq_j;

            // サイコロ i の出目確率
            for (int a : dice[i]) {
                freq_i[a] += 1.0 / K[i];
            }
            // サイコロ j の出目確率
            for (int b : dice[j]) {
                freq_j[b] += 1.0 / K[j];
            }
            
            // 共通の出目で確率を計算
            double currentProbability = 0.0;
            for (const auto &entry : freq_i) {
                int value = entry.first;
                if (freq_j.count(value)) {
                    currentProbability += entry.second * freq_j[value];
                }
            }
            maxProbability = max(maxProbability, currentProbability);
        }
    }

    cout << fixed << setprecision(8) << maxProbability << endl;

    return 0;
} 
