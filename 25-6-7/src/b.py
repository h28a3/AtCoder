def solve():
    N = int(input())
    A = list(map(int, input().split()))

    max_x = 0
    for x in range(N + 1):
        count = sum(1 for a in A if a >= x)
        if count >= x:
            max_x = x

    print(max_x)

solve()
