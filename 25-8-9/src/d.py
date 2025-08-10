def count_even_zero_substrings(S: str) -> int:
    prefix = [0]  # prefix parity of zeros
    for ch in S:
        prefix.append(prefix[-1] ^ (1 if ch == '0' else 0))

    count = [0, 0]
    for p in prefix:
        count[p] += 1

    # 同じprefixの組み合わせの数を合計
    ans = count[0] * (count[0] - 1) // 2 + count[1] * (count[1] - 1) // 2
    return ans

# 入力例
n = int(input())
S = input()
print(count_even_zero_substrings(S))
