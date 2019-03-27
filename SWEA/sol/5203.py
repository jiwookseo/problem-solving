# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 D3
def check(count):
    flag = 0
    for num in count:
        if num >= 3:
            return True
        elif num > 0:
            flag += 1
            if flag == 3:
                return True
        else:
            flag = 0


for TC in range(1, int(input()) + 1):
    m = map(int, input().split())
    odd = 1
    a = [0] * 10
    b = [0] * 10
    draw = True
    for i in m:
        if odd:
            a[i] += 1
            if check(a):
                print("#{} 1".format(TC))
                draw = False
                break
        else:
            b[i] += 1
            if check(b):
                print("#{} 2".format(TC))
                draw = False
                break
        odd = 1 - odd
    if draw:
        print("#{} 0".format(TC))
