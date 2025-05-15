n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    a_set = set(a)
    a_sort = sorted(a)
    if len(a_set) != m:
        print(ans)
        exit()
    ans += 1
    a.pop(-1)
print(ans)
