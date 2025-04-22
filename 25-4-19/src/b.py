import queue

n = int(input())
q = queue.Queue()
for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        q.put(tmp[1])
    else:
        print(q.get())
