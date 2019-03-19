# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 D2
for tc in range(1, int(input()) + 1):
    inp = input().split()
    n = int(inp[0])
    ans = ''
    for i in range(n):
        for j in range(3, -1, -1):
            ans += '1' if int(inp[1][i],16) & ( 1 << j ) else '0'
    print("#{} {}".format(tc, ans))
