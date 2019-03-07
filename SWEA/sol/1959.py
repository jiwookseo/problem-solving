# 1959. 두 개의 숫자열 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE
for tc in range(1,int(input())+1):
    i = input().split()
    n, m = int(i[0]), int(i[1])
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n == m:
        result = sum([a[i] * b[i] for i in range(n)])
    else:
        result = 0
        if n < m:
            n, m = m, n
            a, b = b, a
        else:
            for i in range(n-m+1):
                temp = 0
                for j in range(m):
                    temp += a[i + j] * b[j]
                if temp > result:
                    result = temp
    print("#{} {}".format(tc, result))
