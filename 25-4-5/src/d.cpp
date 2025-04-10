#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int main() {
    int h, w;
    cin >> h >> w;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    int a, b, c, d;
    cin >> a >> b >> c >> d;
    --a; --b; --c; --d; // 0-indexedに調整

    // 方向ベクトル (上下左右)
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    // BFSのためのキューと距離配列
    deque<pair<int, int>> q;
    q.push_front({a, b});
    vector<vector<int>> distance(h, vector<int>(w, -1));
    distance[a][b] = 0;

    // BFSループ
    while (!q.empty()) {
        int x, y;
        tie(x, y) = q.front();
        q.pop_front();

        // 普通の移動 (道が続いていれば移動)
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < h && ny >= 0 && ny < w && grid[nx][ny] == '.' && distance[nx][ny] == -1) {
                distance[nx][ny] = distance[x][y];
                q.push_front({nx, ny});
            }
        }

        // 前蹴り (壁を壊す)
        for (int i = 0; i < 4; ++i) {
            for (int j = 1; j <= 2; ++j) { // 1つ前と2つ前
                int nx = x + dx[i] * j;
                int ny = y + dy[i] * j;
                if (nx >= 0 && nx < h && ny >= 0 && ny < w && grid[nx][ny] == '#' && distance[nx][ny] == -1) {
                    // 壁を道に変えた場合、前蹴りの回数を増やす
                    distance[nx][ny] = distance[x][y] + 1;
                    q.push_back({nx, ny});
                }
            }
        }
    }

    // 終了位置にたどり着くまでの最小前蹴り回数
    cout << distance[c][d] << endl;

    return 0;
}
