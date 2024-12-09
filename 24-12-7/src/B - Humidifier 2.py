def shokika(yuka,h,w):
    for i in range(h):
        for j in range(w):
            yuka[i][j]=0
    return yuka

[h,w,d] = list(map(int,input().split()))
s=[]
yuka=[]
for i in range(h):
    s.append(input())
    yuka.append([0]*w)
index =[]
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            index.append((i,j))

l=len(index)
max=0
for i in range(l-1):
    for j in range(i+1,l):
        yuka=shokika(yuka,h,w)
        cnt=0
        for x in range(h):
            for y in range(w):
                if (abs(x-index[i][0])+abs(y-index[i][1])<=d or abs(x-index[j][0])+abs(y-index[j][1])<=d) and s[x][y] == ".":
                    yuka[x][y]=1
            cnt+=yuka[x].count(1)
        if max<cnt:
            max=cnt
print(max)
