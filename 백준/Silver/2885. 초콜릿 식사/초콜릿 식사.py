import sys 

k = int(sys.stdin.readline())

t = 1
cnt = 0

while k > t:
  t *= 2

tmp = t

while True:
  if k % t == 0:
    break

  else:
    t //= 2
    cnt += 1
  
  

print(tmp, cnt)