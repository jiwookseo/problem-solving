# https://programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    n = len(B)
    B.sort()
    maxi = B[-1]
    mini = B[0]
    for a in A:
        n = len(B)
        if a > maxi:
            del B[0]
            continue
        elif a < mini:
            del B[0]
            answer += 1
            continue
        i = 0
        while i < n:
            if B[i] > a:
                break
            i += 1
        if i == n:
            del B[0]
        else:
            del B[i]
            answer += 1
    return answer