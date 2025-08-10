import sys
from collections import defaultdict
from math import gcd

def solve():
    input = sys.stdin.readline
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    slope_counts = defaultdict(int)
    midpoint_counts = defaultdict(int)

    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]

            # 傾きを簡約化して表現
            dx = x2 - x1
            dy = y2 - y1

            if dx == 0:
                slope = (1, 0)  # 垂直線
            elif dy == 0:
                slope = (0, 1)  # 水平線
            else:
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx = -dx
                    dy = -dy
                slope = (dx, dy)

            slope_counts[slope] += 1

            # 中点の2倍座標（整数で扱う）
            mid_x = x1 + x2
            mid_y = y1 + y2
            midpoint_counts[(mid_x, mid_y)] += 1

    # 平行な辺の組の数（k本の直線からkC2通り）
    total_parallel_pairs = 0
    for v in slope_counts.values():
        if v >= 2:
            total_parallel_pairs += v * (v - 1) // 2

    # 平行四辺形の数（同じ中点のペアがk個あればkC2通り）
    parallelograms = 0
    for v in midpoint_counts.values():
        if v >= 2:
            parallelograms += v * (v - 1) // 2

    # 台形の数 = 平行な辺の組数 - 平行四辺形の数
    answer = total_parallel_pairs - parallelograms
    print(answer)

if __name__ == "__main__":
    solve()
