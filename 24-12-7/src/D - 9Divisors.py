import math

def count_numbers_with_9_divisors(N):
    # 素数リストをエラトステネスの篩で生成
    def sieve(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [x for x in range(limit + 1) if is_prime[x]]

    # 素数を十分な範囲で生成
    sqrt_N = int(math.sqrt(N)) + 1
    primes = sieve(sqrt_N)
    
    count = 0

    # パターン1: p^8 <= N
    for p in primes:
        if p**8 <= N:
            count += 1
        else:
            break

    # パターン2: p1^2 * p2^2 <= N
    for i in range(len(primes)):
        p1 = primes[i]
        if p1**2 > N:
            break
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if p1**2 * p2**2 <= N:
                count += 1
            else:
                break

    return count

# 入力
N = int(input())
result = count_numbers_with_9_divisors(N)
print(result)
