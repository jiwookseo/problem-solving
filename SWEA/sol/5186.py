# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2
for tc in range(1, int(input()) + 1):
    num = float(input())
    result = ''
    for _ in range(12):
        num *= 2
        if num >= 1:
            result += '1'
            num -= 1
        else:
            result += '0'
        if num == 0:
            break
    print("#{} {}".format(tc, result if num == 0 else "overflow"))
