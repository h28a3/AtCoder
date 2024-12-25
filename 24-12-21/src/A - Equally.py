def can_divide_into_equal_sums(a, b, c):
    # グループの和が等しいか確認
    if a == b + c or b == a + c or c == a + b or (a == b and a == c):
        return "Yes"
    else:
        return "No"

# 入力を受け取る
a, b, c = map(int, input().split())

# 判定して出力
print(can_divide_into_equal_sums(a, b, c))
