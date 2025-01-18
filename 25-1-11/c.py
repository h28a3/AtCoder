#import enumerate
n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i, num in enumerate(a):
    left, right = i + 1, n - 1
    while left <= right:
      mid = (left + right) // 2
      if a[mid] >= num * 2:
        right = mid - 1
      else:
        left = mid + 1
    cnt += n - left
print(cnt)
