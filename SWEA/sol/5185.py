# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 D2
for tc in range(1, int(input()) + 1):
    i = input().split()
    n = int(i[0])
    result = "".join(['1' if int(i[1][j][k], 16) & (1 << k) else '0' for k in range(3, -1, -1) for j in range(n)])
    print("#{} {}".format(tc, result))
