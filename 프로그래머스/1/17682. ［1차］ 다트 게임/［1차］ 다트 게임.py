def solution(dartResult):
    answer = 0
    res = []
    cnt = 0
    dartResult = dartResult.replace("10","t")
    for n in dartResult:
        if n.isnumeric():
            cnt += int(n)
            continue
        elif n == "t":
            cnt += 10
            continue
        elif n == "S":
            res.append(cnt)
        elif n == "D":
            res.append(cnt**2)
        elif n == "T":
            res.append(cnt**3)
        elif n == "*":
            if len(res) > 1:
                res[-1] *= 2
                res[-2] *= 2
            else:
                res[-1] *= 2
        elif n == "#":
            res[-1] *= -1
        cnt = 0
        
                
    return sum(res)