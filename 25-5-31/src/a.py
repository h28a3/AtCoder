n, s = map(int, input().split())
t = list(map(int, input().split()))
if t[0] > s:
    print("No")
    exit()
for i in range(1, len(t)):
    if t[i] - t[i-1] > s:
        print("No")
        exit()
print("Yes")
