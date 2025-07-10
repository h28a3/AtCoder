def count_unique_concatenations(strings):
    result_set = set()
    n = len(strings)
    for i in range(n):
        for j in range(n):
            if i != j:
                result_set.add(strings[i] + strings[j])
    return len(result_set)

# 入力読み取り
n = int(input())
strings = [input().strip() for _ in range(n)]

# 出力
print(count_unique_concatenations(strings))
