# https://programmers.co.kr/learn/courses/30/lessons/49995
# 채점 결과
# 정확성: 66.7
# 효율성: 0.0
# 합계: 66.7 / 100.0


def solution(cookie):
    answer = 0
    n = len(cookie)
    for l in range(n - 1):
        h = cookie[l]
        for r in range(l + 1, n):
            h += cookie[r]
            a = 0
            b = h
            if h % 2:
                continue
            for m in range(l, r):
                if answer >= b:
                    break
                a += cookie[m]
                b -= cookie[m]
                if a == b:
                    answer = a
    return answer
