# 1946. 간단한 압축 풀기 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq&categoryId=AV5PmkDKAOMDFAUq&categoryType=CODE
for tc in range(1, int(input())+1):
    n = int(input())
    s = ""
    for _ in range(n):
        i = input().split()
        s += i[0] * int(i[1])
    t = 0
    print("#{}".format(tc))
    while len(s) > t:
        print(s[t:min(t + 10, len(s))])
        t += 10
