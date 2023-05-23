def solution(s, skip, index):
    answer = ""
    
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" # 알파벳
    
    for i in skip: # ch => skip의 문자 하나하나
        if i in alpha:
            alpha = alpha.replace(i, "") # 알파벳 안에 skip 문자들 제거
    
    for ss in s:
        change = alpha[(alpha.index(ss) + index) % len(alpha)] # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change
    
    return answer