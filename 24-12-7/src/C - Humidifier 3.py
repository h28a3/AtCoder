from collections import deque

def count_humidified_cells(H, W, D, grid):
    # グリッド全体を走査し、加湿器が置かれている位置を記録
    humidifiers = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'H':
                humidifiers.append((i, j))
    
    # 加湿されるかどうかを記録するための2次元配列
    visited = [[False] * W for _ in range(H)]
    
    # BFSで湿らせる範囲を探索
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右の移動方向
    queue = deque()

    # 加湿器の位置をキューに追加し、初期状態を訪問済みに設定
    for hi, hj in humidifiers:
        queue.append((hi, hj, 0))  # (i, j, 距離)
        visited[hi][hj] = True

    while queue:
        x, y, dist = queue.popleft()
        # 現在の距離がDを超える場合、これ以上探索しない
        if dist >= D:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    # 加湿されたマスの数をカウント
    humidified_count = sum(sum(row) for row in visited)
    return humidified_count


# 入力の処理
if __name__ == "__main__":
    H, W, D = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    result = count_humidified_cells(H, W, D, grid)
    print(result)
