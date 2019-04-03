# 1952. [모의 SW 역량테스트] 수영장
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq&categoryType=CODE
import math


def brute(i=0):
    global t, c, plan, result
    if i >= y:
        temp = sum([plan[j] for j in range(y) if not t[j]])
        temp += math.ceil(sum(t) / 3) * c
        if result > temp:
            result = temp
        return
    t[i] = False
    brute(i + 1)
    if i < y - 2:
        t[i] = t[i + 1] = t[i + 2] = True
    elif i == y - 2:
        t[i] = t[i + 1] = True
    else:
        t[i] = True
    brute(i + 3)


for TC in range(1, int(input()) + 1):
    a, b, c, result = map(int, input().split())
    m = int(b / a)
    inp = input().split()
    while '0' in inp:
        inp.remove('0')
    plan = list(map(int, inp))
    y = len(plan)
    for i in range(y):
        if plan[i] > m:
            plan[i] = b
        elif plan[i]:
            plan[i] *= a
    t = [False] * y
    brute()
    print("#{} {}".format(TC, min(result, sum(plan))))
