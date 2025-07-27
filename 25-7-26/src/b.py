def solve():
    s = input().strip()
    n = len(s)
    s_positions = []
    o_positions = []
    
    # 使える位置の o を記録
    for i in range(n):
        if s[i] == '#':
            s_positions.append(i)
        else:
            o_positions.append(i)

    # 最大の o の配置を構築
    result = ['.'] * n
    for i in s_positions:
        result[i] = '#'
    
    if len(o_positions) > 0:
        result[o_positions[0]] = 'o'
        last_o_pos = o_positions[0]
        
    for pos in o_positions:
        if s[last_o_pos:pos+1].count('#') >= 1:
            result[pos] = 'o'
            last_o_pos = pos

    print(''.join(result))

# 実行
solve()
