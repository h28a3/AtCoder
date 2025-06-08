from collections import Counter

def count_equilateral_triangles(n, l, d):
    if l % 3 != 0:
        return 0

    t = [0]
    for i in range(n - 1):
        t.append((t[-1] + d[i]) % l)

    count = Counter(t)
    x = l // 3
    result = 0

    for a in count:
        b = (a + x) % l
        c = (a + 2 * x) % l
        if b in count and c in count:
            result += count[a] * count[b] * count[c]

    return result // 3

n, l = map(int, input().split())
d = list(map(int, input().split()))
print(count_equilateral_triangles(n, l, d))
