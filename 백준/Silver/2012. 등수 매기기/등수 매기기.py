#1 1 2 3 5

#1 2 3 4 5

import sys 

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
  arr.append(int(sys.stdin.readline()))

arr = sorted(arr)
cnt = 0
for i in range(1, n+1):
  cnt += abs(arr[i-1] - i)

print(cnt)