def solution(k, score):
    answer = []
    
    stack = []
    
    for s in score:
        stack.append(s)
        stack = sorted(stack, reverse=True)[:k]
        answer.append(min(stack))
        
            
    return answer