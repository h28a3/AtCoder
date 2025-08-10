def main():
    S = input().strip()
    n = len(S)
    max_ratio = 0.0

    for i in range(n):
        if S[i] != 't':
            continue
        for j in range(i + 2, n):  # 長さ3以上になるように
            if S[j] != 't':
                continue
            length = j - i + 1
            count_t = S[i:j + 1].count('t')
            ratio = (count_t - 2) / (length - 2)
            if ratio > max_ratio:
                max_ratio = ratio

    print(max_ratio)


if __name__ == "__main__":
    main()
