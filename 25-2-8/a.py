a = list(map(int, input().split()))
a = sorted(a)
if a[0] * a[1] == a[2]:
    print("Yes")
else:
    print("No")
