from itertools import permutations, combinations
def solution(t, p):
    l = len(p)
    p = int(p)
    print(p)
    answer = 0
    for i in range(len(t)):
        if i == len(t) - l + 1:
            break
        if p >= int(t[i:i+l]):
            answer += 1
    
    
    return answer