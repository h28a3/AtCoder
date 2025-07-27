n, l, r = map(int,input().split())
s = input()
if s[l-1:r] == "o"*(r-l+1):
    print("Yes")
else:
    print("No")
