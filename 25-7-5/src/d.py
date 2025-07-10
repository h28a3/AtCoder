from math import gcd
from fractions import Fraction

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    sorted_a = sorted(a, key=abs)
    r = Fraction(sorted_a[1], sorted_a[0])
    set_a = list(set(a))
    if ((n%2 == 0 and a.count(a[0]) == int(n/2)) or (n%2 == 1 and (a.count(a[0]) == int(n/2) + 1 or a.count(a[0]) == int(n/2)))) and len(set_a) == 2 and set_a[1] == -set_a[0]:
        print("Yes")
        continue
    is_gp = True
    for i in range(1, n - 1):
        if sorted_a[i + 1] != sorted_a[i] * r:
            is_gp = False
            break
    print("Yes" if is_gp else "No")
