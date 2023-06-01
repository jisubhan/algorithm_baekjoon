def solution(a, b, n):
    answer = 0
    while n >= a:
        remain_bottles = n % a
        n = (n // a) * b
        answer += n
        n += remain_bottles
    return answer

