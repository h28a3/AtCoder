import itertools

def main():
    # 入力
    N, K, X = map(int, input().split())
    S = [input().strip() for _ in range(N)]
    
    # 1〜N からなる長さ K の数列の全列挙（1-indexedに合わせてインデックス補正）
    all_combinations = itertools.product(range(N), repeat=K)
    
    # 各数列に対して対応する文字列を生成
    strings = []
    for indices in all_combinations:
        combined = ''.join(S[i] for i in indices)
        strings.append(combined)
    
    # 辞書順にソート
    strings.sort()
    
    # X 番目（1-indexed）を出力
    print(strings[X - 1])

if __name__ == "__main__":
    main()
