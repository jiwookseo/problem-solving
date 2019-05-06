# https://programmers.co.kr/learn/courses/30/lessons/12984?language=python3
# 브루트 포스, 시간초과 제외하고는 모두 통과 > 이짙탐색 등을 이용하면 속도는 빠르나 정확한 결과가 나오지 않음.
# 채점 결과
# 정확성: 53.9
# 효율성: 0.0
# 합계: 53.9 / 100.0
from math import inf


def solution(land, P, Q):
    answer = inf
    mini, maxi = land[0][0], land[0][0]
    n = len(land)
    for i in range(n):
        for j in range(n):
            if land[i][j] < mini:
                mini = land[i][j]
            elif land[i][j] > maxi:
                maxi = land[i][j]
    a = maxi - mini + 1
    for m in range(mini, maxi + 1):
        count = 0
        check = True
        for i in range(n):
            for j in range(n):
                t = land[i][j] - m
                count += t * Q if t >= 0 else -t * P
                if count >= answer:
                    check = False
                    break
            if not check:
                break
        if check:
            answer = count
    return answer
