n = int(input())
t = input()
a = input()

for i in range(n):
    if a[i] == "o" and t[i] == "o":
        print("Yes")
        exit()
print("No")
