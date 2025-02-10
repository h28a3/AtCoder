n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

x = []
for i in range(n):
    x.append((p[i], q[i]))
x = sorted(x, reverse=False, key=lambda x: x[1])
for i in range(n):
    print(q[x[i][0]-1], end = " ")
