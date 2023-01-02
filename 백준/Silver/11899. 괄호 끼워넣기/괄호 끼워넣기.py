import sys 

st = sys.stdin.readline()
stack = list()
cnt = 0
for s in st:
  if len(stack) > 0 and stack[-1] == '(' and s == ')':
    stack.pop()
  elif len(stack) == 0 and s == ')':
    cnt += 1
  elif s == '(':
    stack.append(s)

cnt += len(stack)

print(cnt)