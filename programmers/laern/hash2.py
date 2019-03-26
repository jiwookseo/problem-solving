# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(pb):
    l = len(pb)
    for i in range(l - 1):
        for j in range(i + 1, l):
            a, b = pb[i], pb[j]
            check = True
            for k in range(min(len(a), len(b))):
                if a[k] != b[k]:
                    check = False
            if check:
                return False
    return True
