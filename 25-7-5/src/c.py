import sys
input = sys.stdin.readline

from collections import deque

q = int(input())
a = deque()
res = []

for _ in range(q):
    tmp = input().split()
    if tmp[0] == '1':
        c = int(tmp[1])
        x = int(tmp[2])
        # 圧縮追加：末尾と値が同じなら結合
        if a and a[-1][0] == x:
            a[-1] = (x, a[-1][1] + c)
        else:
            a.append((x, c))
    else:
        k = int(tmp[1])
        s = 0
        while k > 0:
            val, cnt = a[0]
            if cnt <= k:
                s += val * cnt
                k -= cnt
                a.popleft()
            else:
                s += val * k
                a[0] = (val, cnt - k)
                k = 0
        res.append(str(s))

print('\n'.join(res))
