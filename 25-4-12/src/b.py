n = int(input())
status = 0
cnt = 0
for i in range(n):
    s = input()
    if s == "login":
        status = 1
    elif s == "logout":
        status = 0
    elif s == "private" and status == 0:
        cnt += 1
print(cnt)
