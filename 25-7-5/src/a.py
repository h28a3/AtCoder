n, m = map(int, input().split())
a = list(map(int, input().split()))

if m >= sum(a):
    print("Yes")
else:
    print("No")
