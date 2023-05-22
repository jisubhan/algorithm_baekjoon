def solution(keymap, targets):
    dic = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k not in dic:
                dic[k] = i + 1
            else:
                dic[k] = min(dic[k], i+1)
    answer = []
    
    for tar in targets:
        clicked = 0
        for t in tar:
            if t not in dic:
                clicked = -1
                break
            clicked += dic[t]
        answer.append(clicked)
    
    return answer