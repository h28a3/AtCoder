#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M; 
    cin >> N >> M;

    vector<vector<pair<int,int>>> graph(N+1);
    for(int i = 0; i < M; i++) {
        int u, v, w; cin >> u >> v >> w;
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, w);
    }

    auto can_reach = [&](int mask) {
        vector<bool> visited(N+1, false);
        queue<int> q;
        q.push(1);
        visited[1] = true;
        while(!q.empty()) {
            int node = q.front(); q.pop();
            if (node == N) return true;
            for (auto& [nxt, w] : graph[node]) {
                if (!visited[nxt] && ((w | mask) == mask)) {
                    visited[nxt] = true;
                    q.push(nxt);
                }
            }
        }
        return false;
    };

    int ans = (1 << 30) - 1;
    for (int bit = 29; bit >= 0; bit--) {
        int candidate = ans & ~(1 << bit);
        if (can_reach(candidate)) {
            ans = candidate;
        }
    }

    cout << ans << "\n";
    return 0;
}
