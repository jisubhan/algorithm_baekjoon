import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(n):
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

x = max(dp)
result = []

for i in range(n-1, -1, -1):
  if dp[i] == x:
    result.append(arr[i])
    x-=1

result.reverse()
for r in result:
  print(r, end=' ')