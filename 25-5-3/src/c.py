import sys
sys.setrecursionlimit(10**6)

def is_cycle_graph(N, M, edges):
    if N != M:
        return False  # 条件1: 辺の数が頂点数と等しくない

    from collections import defaultdict

    graph = defaultdict(list)
    degree = [0] * (N + 1)
    
    # グラフ構築 & 各頂点の次数確認
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    # 条件2: 各頂点の次数が2であるか
    for i in range(1, N + 1):
        if degree[i] != 2:
            return False

    # 条件3: グラフが連結であるか (DFSで確認)
    visited = [False] * (N + 1)

    def dfs(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs(u)

    dfs(1)

    if not all(visited[1:]):
        return False

    return True


# 入力部分
def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    if is_cycle_graph(N, M, edges):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
