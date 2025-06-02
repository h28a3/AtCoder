def min_flips_to_make_ones_continuous(n: int, s: str) -> int:
    prefix_1 = [0] * (n + 1)  # 1の累積和

    # prefix_1[i] = s[0:i] に含まれる1の数
    for i in range(n):
        prefix_1[i + 1] = prefix_1[i] + (1 if s[i] == '1' else 0)

    total_ones = prefix_1[n]
    
    # 区間 [l, r) を選んで、その中を1にし、外の1を0に反転
    # 反転回数 = (区間内の0の数) + (区間外の1の数)
    #          = (r - l - (prefix_1[r] - prefix_1[l])) + (total_ones - (prefix_1[r] - prefix_1[l]))
    #          = (r - l) + total_ones - 2 * (prefix_1[r] - prefix_1[l])
    #          = total_ones + (r - 2 * prefix_1[r]) - (l - 2 * prefix_1[l])

    # ここで、value_optimized(i) = i - 2 * prefix_1[i] と定義する。
    # 目的は total_ones + value_optimized(r) - value_optimized(l) を最小化すること。
    # すなわち、value_optimized(r) - value_optimized(l) を最小化する。
    # ここで l < r である。

    min_flips_delta = float('inf')
    
    # value_optimized(0) は l=0 の場合に対応
    # 最初の l が 0 なので、max_val_so_far は value_optimized(0) で初期化
    max_val_so_far = 0 - 2 * prefix_1[0] # = 0
    
    # r を 1 から n までループ
    for r in range(1, n + 1):
        # 現在の r に対して、過去の最大の value_optimized(l) を使って差を計算
        current_value_r = r - 2 * prefix_1[r]
        min_flips_delta = min(min_flips_delta, current_value_r - max_val_so_far)
        
        # 次のループのために max_val_so_far を更新
        max_val_so_far = max(max_val_so_far, current_value_r)
    
    # 全ての1を0にする（空の連続する1の区間）場合も考慮
    # この場合、必要な反転回数は total_ones
    # min_flips_delta が infinity の場合、これは empty string, or some edge case where loop doesn't run.
    # min_flips_delta は少なくとも 0 (l=rの場合に相当) を含むべきなので、
    # total_ones が初期の最小値として適切。
    # min_flips_delta = min(min_flips_delta, 0) # l=rの場合を考慮、total_onesを直接返す

    # 区間を空にする場合は、total_ones の反転が必要。
    # 上記のループでは、l=r のケース (delta=0) は直接的にカバーされていない。
    # 例えば、N=1, s="0" の場合、total_ones=0 で、min_flips_delta は inf のまま。
    # total_ones + 0 = 0 となるべき。

    # そこで、min_flips_deltaの初期値を0に設定するか、
    # 最終的な結果を max(total_ones, total_ones + min_flips_delta) で計算する。
    # いや、min_flips_deltaは負の値も取りうるので、
    # 最終的な結果は total_ones + min_flips_delta。
    # total_ones を初期値として min_flips_result に入れる。
    
    # 最終的な答えは total_ones + (r - 2 * prefix_1[r]) - (l - 2 * prefix_1[l]) の最小値
    # つまり、total_ones + min_flips_delta
    
    # ここでの min_flips_delta は、value_optimized(r) - value_optimized(l) の最小値である。
    # l=r の場合、delta は 0 となる。このケースは、max_val_so_far を適切に更新していれば、
    # 0 となる場合も考慮されるべき。
    # 例: s = "101", n=3
    # prefix_1 = [0, 1, 1, 2]
    # total_ones = 2
    # value_optimized:
    # i=0: 0 - 2*0 = 0 (max_val_so_far = 0)
    # i=1: 1 - 2*1 = -1. min_flips_delta = min(inf, -1 - 0) = -1. max_val_so_far = max(0, -1) = 0.
    # i=2: 2 - 2*1 = 0. min_flips_delta = min(-1, 0 - 0) = -1. max_val_so_far = max(0, 0) = 0.
    # i=3: 3 - 2*2 = -1. min_flips_delta = min(-1, -1 - 0) = -1. max_val_so_far = max(0, -1) = 0.
    # result = total_ones + min_flips_delta = 2 + (-1) = 1.
    # これは "101" -> "000" (2 flips) もしくは "111" (1 flip for 0) -> "111" (no flips outside) = 1 flip (0 to 1).
    # "101" を "111" にする場合、真ん中の0を1にする (1反転)。total_onesは2なので、
    # (r-l) - (ones_inside) + (total_ones - ones_inside)
    # l=1, r=2, 区間 "0"
    # zeros_inside = 1
    # ones_inside = 0
    # ones_outside = 2 - 0 = 2
    # flips = 1 + 2 = 3. 
    # これは違う。

    # 計算式の見直し:
    # flips = zeros_inside + ones_outside
    # zeros_inside = (r - l) - (prefix_1[r] - prefix_1[l])
    # ones_outside = total_ones - (prefix_1[r] - prefix_1[l])
    # flips = (r - l) - (prefix_1[r] - prefix_1[l]) + total_ones - (prefix_1[r] - prefix_1[l])
    # flips = total_ones + (r - l) - 2 * (prefix_1[r] - prefix_1[l])
    # flips = total_ones + (r - 2*prefix_1[r]) - (l - 2*prefix_1[l])

    # ここで、f(k) = k - 2 * prefix_1[k] とする。
    # flips = total_ones + f(r) - f(l)
    # この f(r) - f(l) を最小化したい。
    # min_flips = total_ones + min_{0 <= l < r <= n} (f(r) - f(l))
    # ただし、l=r のケースも考慮する必要がある。
    # l=r の場合、連続する1の区間を空にする。この場合の反転回数は total_ones.
    # f(r) - f(l) = 0 となるので、total_ones + 0 = total_ones.
    # これは、min_flips_delta の初期値として 0 を含めることで対処できる。
    # 例えば、min_flips_delta = 0 と初期化し、ループ内で更新すれば良い。

    min_flips_delta = 0 # l=r の場合 (連続する1の区間を空にする)
    
    # f(k) = k - 2 * prefix_1[k]
    # max_f_l は、l の範囲 [0, r-1] での f(l) の最大値
    max_f_l = 0 - 2 * prefix_1[0] # f(0) = 0
    
    for r in range(1, n + 1):
        # f(r) の値を計算
        current_f_r = r - 2 * prefix_1[r]
        
        # f(r) - max_f_l を計算して最小値を更新
        min_flips_delta = min(min_flips_delta, current_f_r - max_f_l)
        
        # max_f_l を更新 (次の r のために)
        # 現在の r の f(r) の値も max_f_l の候補になる
        max_f_l = max(max_f_l, current_f_r)

    return total_ones + min_flips_delta

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    s = input()
    results.append(min_flips_to_make_ones_continuous(n, s))

for res in results:
    print(res)
