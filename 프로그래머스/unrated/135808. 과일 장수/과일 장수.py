def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    temp_m = m - 1
    for i in range(0+temp_m, len(score), m):
        answer += (score[i] * m)
    return answer