n, d = list(map(int, input().split()))
t = []
l = []
for i in range(n):
    tmp = list(map(int, input().split()))
    t.append(tmp[0])
    l.append(tmp[1])

for i in range(1,d+1):
    ans = []
    for j in range(n):
        ans.append(t[j]*(l[j]+i))
    print(max(ans))
