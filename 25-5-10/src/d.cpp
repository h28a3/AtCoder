#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int H, W;
vector<string> grid;
vector<string> result;

// 上下左右の移動
const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};
const char arrow[4] = {'^', 'v', '<', '>'};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> H >> W;
    grid.resize(H);
    result.resize(H);

    for (int i = 0; i < H; ++i) {
        cin >> grid[i];
        result[i] = string(W, '.'); // 初期化
    }

    queue<pair<int, int>> q;

    // 初期化：壁と非常口を処理
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (grid[i][j] == '#') {
                result[i][j] = '#';
            } else if (grid[i][j] == 'E') {
                result[i][j] = 'E';
                q.emplace(i, j);
            }
        }
    }

    // BFS開始
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();

        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (nx >= 0 && nx < H && ny >= 0 && ny < W) {
                if (grid[nx][ny] == '.' && result[nx][ny] == '.') {
                    // 逆方向の矢印を貼る（どの方向から来たか）
                    int rx = x - nx, ry = y - ny;
                    for (int rdir = 0; rdir < 4; ++rdir) {
                        if (dx[rdir] == rx && dy[rdir] == ry) {
                            result[nx][ny] = arrow[rdir];
                            break;
                        }
                    }
                    q.emplace(nx, ny);
                }
            }
        }
    }

    // 出力
    for (int i = 0; i < H; ++i) {
        cout << result[i] << '\n';
    }

    return 0;
}
