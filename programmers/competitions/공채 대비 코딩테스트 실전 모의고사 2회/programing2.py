import math
def solution(l, v):
    v.sort()
    maximum=max(abs(v[0]-0),abs(v[-1]-l))*2
    a=v[1:]
    b=v[:-1]
    for i in range(len(a)):
        if maximum < a[i]-b[i]:
            maximum = a[i]-b[i]
    return math.ceil(maximum/2)

"""
채점 결과
정확성: 70.0
효율성: 30.0
합계: 100.0 / 100.0
"""