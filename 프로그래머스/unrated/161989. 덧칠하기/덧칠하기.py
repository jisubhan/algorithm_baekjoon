def solution(n, m, section):
    answer = 0
    arr = [1] * n
    for s in section:
        arr[s-1] = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(m):
                if i + j < len(arr):
                    arr[i+j] = 1
            answer += 1
    return answer