import bisect

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    
    from collections import deque
    b_deque = deque(b)

    total_sum = 0
    used_b = [False] * n # Bの要素が使われたかどうかのフラグ

    import collections
    b_counts = collections.Counter(b)
    # B をソートしてリストに変換しておく (bisect_left で使うため)
    b_unique_sorted = sorted(b_counts.keys())

    total_min_sum = 0
    for val_a in a:
        idx_ge_target = bisect.bisect_left(b_unique_sorted, m - val_a)
        
        best_b = -1 # 見つからなかった場合
        min_mod_val = m + 1 # 最小の (A_i + B_j) % M

        candidates_b_indices = []
        if idx_ge_target < len(b_unique_sorted):
            candidates_b_indices.append(idx_ge_target)
        if idx_ge_target > 0:
            candidates_b_indices.append(idx_ge_target - 1)
        
        # 候補となる B の要素の中から、実際に使用できる (count > 0) ものを探す
        current_best_b_val = -1
        current_min_mod_val = m + 1

        for cand_idx in candidates_b_indices:
            cand_b_val = b_unique_sorted[cand_idx]
            if b_counts[cand_b_val] > 0:
                mod_val = (val_a + cand_b_val) % m
                if mod_val < current_min_mod_val:
                    current_min_mod_val = mod_val
                    current_best_b_val = cand_b_val
                elif mod_val == current_min_mod_val:
                    pass
        
    a.sort()
    b.sort() # Bも昇順にソート

    b_ptr_left = 0
    b_ptr_right = n - 1
    
    total_min_mod_sum = 0
    
    for a_val in a:
        # A_i と Bの左端を組み合わせた場合
        val_from_left = (a_val + b[b_ptr_left]) % m
        
        # A_i と Bの右端を組み合わせた場合
        val_from_right = (a_val + b[b_ptr_right]) % m
        
        if val_from_left < val_from_right:
            total_min_mod_sum += val_from_left
            b_ptr_left += 1
        else:
            total_min_mod_sum += val_from_right
            b_ptr_right -= 1
            
    print(total_min_mod_sum)


t = int(input())
for _ in range(t):
    solve()
