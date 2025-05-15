def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))

    total_sum = sum(A)
    total_square_sum = sum(x * x for x in A)

    result = (total_sum * total_sum - total_square_sum) // 2
    print(result)

if __name__ == "__main__":
    main()
