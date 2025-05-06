def rotate_90(grid):
    N = len(grid)
    return [''.join(grid[N - j - 1][i] for j in range(N)) for i in range(N)]

def count_diff(grid1, grid2):
    return sum(1 for i in range(len(grid1)) for j in range(len(grid1)) if grid1[i][j] != grid2[i][j])

def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]
    T = [input().strip() for _ in range(N)]

    min_operations = float('inf')
    current_S = S[:]

    for rotation in range(4):
        diff_count = count_diff(current_S, T)
        total_operations = rotation + diff_count
        min_operations = min(min_operations, total_operations)
        current_S = rotate_90(current_S)

    print(min_operations)

if __name__ == "__main__":
    main()
