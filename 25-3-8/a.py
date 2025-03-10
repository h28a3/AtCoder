n = int(input())
a = list(map(int, input().split()))

flag = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        flag += 1
    else:
        flag = 0
    if flag == 2:
        print("Yes")
        exit()
print("No")
