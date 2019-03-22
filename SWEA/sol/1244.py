# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE
for tc in range(1, int(input()) + 1):
    i = input().split()
    k = int(i[1])
    n = len(i[0])
    temp = [(list(i[0]), 0, 0)]
    result = '0' * n
    while temp:
        num, i, t = temp.pop()
        if t == k:
            tt = "".join(num)
            if result < tt:
                result = tt
        elif i == n:
            if (k - t) % 2 and n == len(set(num)):
                num[-1], num[-2] = num[-2], num[-1]
            tt = "".join(num)
            if result < tt:
                result = tt
        else:
            m = max(num[i:])
            c = num[i]
            if m == c:
                temp.append((num[:], i + 1, t))
            else:
                num[i] = m
                for j in range(i + 1, n):
                    if num[j] == m:
                        temp.append((num[:j] + [c] + num[j + 1:], i + 1, t + 1))
    print("#{} {}".format(tc, result))
