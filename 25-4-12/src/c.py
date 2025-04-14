MOD = 10**9

def kbonacci(n, k):
    if n < k:
        return 1

    A = [1] * k
    window_sum = k  # A[0]〜A[k-1] はすべて 1

    for i in range(k, n + 1):
        A.append(window_sum % MOD)
        window_sum = (window_sum + A[-1] - A[-k-1]) % MOD

    return A[n]

n, k = map(int, input().split())
print(kbonacci(n, k))
