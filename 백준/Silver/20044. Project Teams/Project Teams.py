import sys

n = int(sys.stdin.readline())

arr = sorted(list(map(int, sys.stdin.readline().split())))


min = arr[0] + arr[-1]
k = 2*n-1
for i in range(1, k-1):
  if arr[i] + arr[k-i] < min:
    min = arr[i] + arr[k-i]

print(min)
