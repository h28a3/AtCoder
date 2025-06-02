def solve_domino_problem(H, W, A):
    from collections import defaultdict

    N = H * W
    id = lambda i, j: i * W + j
    flat_A = [A[i][j] for i in range(H) for j in range(W)]

    # ドミノ候補（横・縦）
    dominoes = []
    for i in range(H):
        for j in range(W):
            if j + 1 < W:
                dominoes.append((id(i, j), id(i, j + 1)))
            if i + 1 < H:
                dominoes.append((id(i, j), id(i + 1, j)))

    from functools import lru_cache

    # 初期状態: すべて未使用 → 全体XORを取る
    total_xor = 0
    for v in flat_A:
        total_xor ^= v

    dp = dict()
    dp[0] = total_xor  # 状態0（何も置いてない）でのスコア

    for mask in range(1 << N):
        if mask not in dp:
            continue
        current_score = dp[mask]
        for a, b in dominoes:
            if ((mask >> a) & 1) or ((mask >> b) & 1):
                continue  # すでに使われている
            new_mask = mask | (1 << a) | (1 << b)
            new_score = current_score ^ flat_A[a] ^ flat_A[b]
            if new_mask not in dp or dp[new_mask] < new_score:
                dp[new_mask] = new_score

    print(max(dp.values()))

# 入力読み取り部分
def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    solve_domino_problem(H, W, A)

if __name__ == "__main__":
    main()
