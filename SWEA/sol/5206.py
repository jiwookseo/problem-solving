# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 D3
def check(start, end, item, flag=None):
    global a, result
    m = (start + end) // 2
    p = a[m]
    if item == p:
        result += 1
        return
    elif start == end:
        return
    elif item < p:
        if flag == 1:
            return
        else:
            check(start, m - 1, item, 1)
    else:
        if flag == 2:
            return
        else:
            check(m + 1, end, item, 2)


for TC in range(1, int(input()) + 1):
    n = int(input().split()[0])
    a = sorted(map(int, input().split()))
    b = map(int, input().split())
    result = 0
    for i in b:
        check(0, n - 1, i)
    print("#{} {}".format(TC, result))
