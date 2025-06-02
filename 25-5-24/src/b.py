def solve(x, y):
    total = 0
    satisfying = 0

    for a in range(1, 7):       # サイコロ1の出目
        for b in range(1, 7):   # サイコロ2の出目
            total += 1
            if a + b >= x or abs(a - b) >= y:
                satisfying += 1

    probability = satisfying / total
    print(probability)

# 標準入力から読み込む場合
if __name__ == "__main__":
    X, Y = map(int, input().split())
    solve(X, Y)
