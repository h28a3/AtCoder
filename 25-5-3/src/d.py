import sys
import itertools

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    C = list(map(int, data[idx:idx+N]))
    idx += N

    # animal_in_zoos[i] = 動物iを見られる動物園のリスト（0-indexed）
    animal_in_zoos = [[] for _ in range(M)]
    zoo_to_animals = [set() for _ in range(N)]
    for i in range(M):
        K = int(data[idx])
        idx += 1
        for _ in range(K):
            zoo = int(data[idx]) - 1
            idx += 1
            animal_in_zoos[i].append(zoo)
            zoo_to_animals[zoo].add(i)

    # 動物を1匹も見られない動物園を除去（高速化）
    useful_zoos = [i for i in range(N) if zoo_to_animals[i]]
    zoo_count = len(useful_zoos)

    min_cost = float('inf')
    for visits in itertools.product((0, 1, 2), repeat=zoo_count):
        seen = [0] * M
        for idx_in_list, zoo_id in enumerate(useful_zoos):
            times = visits[idx_in_list]
            if times == 0:
                continue
            for animal_id in zoo_to_animals[zoo_id]:
                seen[animal_id] += times
        # 2回未満の動物があればスキップ（早期終了）
        for count in seen:
            if count < 2:
                break
        else:
            total = sum(visits[i] * C[useful_zoos[i]] for i in range(zoo_count))
            min_cost = min(min_cost, total)

    print(min_cost)

if __name__ == "__main__":
    main()
