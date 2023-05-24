def solution(s):
    answer = []
    dic = {}
    for i, k in enumerate(s):
        if k not in dic:
            dic[k] = i
            answer.append(-1)
        else:
            answer.append(i - dic[k])
            dic[k] = i
            
    print(dic)
    print(answer)
    return answer