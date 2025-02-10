n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
rest = n - m
print(rest)
for i in range(1, n+1):
    if not(i in a):
        print(i, end = " ")
if rest == 0:
    print()
