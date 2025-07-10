import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def solve():
    T = int(input())
    results = []

    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))

        def dfs(l, r):
            if r - l == 1:
                return [P[l]]

            m = (l + r) // 2
            left = dfs(l, m)
            right = dfs(m, r)

            # 並べる順番で辞書順を比較して最小になるように反転
            if right + left < left + right:
                return right + left
            else:
                return left + right

        ans = dfs(0, 1 << N)
        results.append(" ".join(map(str, ans)))

    print("\n".join(results))

solve()
