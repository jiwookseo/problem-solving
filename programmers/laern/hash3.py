# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    cd = dict()
    for i, j in clothes:
        if j in cd:
            cd[j] += 1
        else:
            cd[j] = 1
    answer = 1
    for i in cd.values():
        answer *= (i + 1)
    return answer - 1
