n=int(input())
t=[]
v=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    t.append(tmp[0])
    v.append(tmp[1])
ans=0
for i in range(n-1):
    ans+=v[i]
    ans-=t[i+1]-t[i]
    if ans<0:
        ans=0
print(v[-1]+ans)
