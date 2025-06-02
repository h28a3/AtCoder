n, m = map(int, input().split())
diff = [0] * (n + 2)

for _ in range(m):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = a[i - 1] + diff[i]

print(min(a[1:]))
