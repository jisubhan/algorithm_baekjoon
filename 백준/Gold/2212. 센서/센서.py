import sys 

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dist = list(map(int, sys.stdin.readline().split()))
dist = sorted(dist)
if k >= n:
  print(0)
  sys.exit()
length = []
for i in range(1, n):
  length.append(dist[i] - dist[i-1])

length = sorted(length, reverse = True)
for _ in range(k-1):
  length.pop(0)

print(sum(length))