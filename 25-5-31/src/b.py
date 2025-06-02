n = int(input())
a = list(map(int, input().split()))

b = sorted(set(a))
print(len(b))
for i in b:
    print(i, end = " ")
