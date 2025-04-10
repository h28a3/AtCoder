n, m = map(int, input().split())
if n == 1:
    print(m+1)
else:
    s = (n**(m+1)-1)
    if s > (n-1)*10**9:
        print("inf")
    else:
        print(int(s/(n-1)))
