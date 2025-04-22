n, m = map(int, input().split())
a = []
need = [set() for _ in range(m)]
for i in range(m):
    tmp = list(map(int, input().split()))
    need[i] = set(tmp[1:])

b = list(map(int, input().split()))

# bの要素が出現する位置を記録
pos = {}
for i, val in enumerate(b):
    pos.setdefault(val, []).append(i)

# 各a[j] が満たされる最も早い位置を調べる
satisfy_time = [n] * m  # n以降なら一生満たされない扱い
for j in range(m):
    indices = []
    for val in need[j]:
        if val not in pos:
            break  # 満たされない
        indices.append(pos[val][0])  # 最初に現れる位置を記録
    else:
        satisfy_time[j] = max(indices)

# 各位置 i に対していくつ満たされたかを累積
res = [0] * (n + 1)
for t in satisfy_time:
    if t < n:
        res[t] += 1

# 累積和を取って答えを得る
for i in range(1, n):
    res[i] += res[i - 1]

for i in range(n):
    print(res[i])
