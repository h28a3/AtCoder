import sys
import bisect

input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# 累積和
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + a[i]

total_sum = prefix[n]  # sum(a)

for _ in range(q):
    b = int(input())
    # b-1 より小さい要素の個数を二分探索
    idx = bisect.bisect_left(a, b)
    
    # min(a[i], b-1) の総和を計算
    sum_min = prefix[idx] + (n - idx) * (b - 1)
    
    if sum_min < total_sum:
        print(sum_min + 1)
    else:
        print(-1)
