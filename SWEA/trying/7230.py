# 7230. 현호의 자물쇠따기 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWlQWJMKuHoDFAVS
# permutation 을 이용한 완전검색으로는 100개 TC 중 1개 밖에 Pass 할 시간이 주어지지 않는다. (10초)
# 배수판별식을 이용해 가지치기를 진행, 똑같은 결과


def permute(li, i):
    global count, n, k
    # permutation 완료, 검증
    if i == n:
        res = ''
        for j in li:
            res += str(j)
        if int(res) % k == 0:
            count += 1
    # i번째 원소 고정 과정
    for j in range(i, n):
        li[i], li[j] = li[j], li[i]
        permute(li, i + 1)
        li[i], li[j] = li[j], li[i]
    return


def fac(x):
    global f
    l = len(f)
    if l <= x:
        temp = f[-1]
        for i in range(l, x + 1):
            temp *= i
            f.append(temp)
    return f[x]


f = [1, 1, 2, 6, 24, 120, 720]
for tc in range(1, int(input()) + 1):
    n = int(input())
    num = list(map(int, input().split()))
    k = int(input())
    if n == 1:
        count = 1 if num[0] % k == 0 else 0
    elif k == 1:
        count = fac(n)
    elif k == 2:
        even = 0
        for i in num:
            if i % 2 == 0:
                even += 1
        count = fac(n - 1) * even  # 마지막 자리만 짝수면 나머지는 관계 없다.
    elif k == 3:
        digit = 0
        for i in num:
            for j in str(i):
                digit += int(j)  # 자릿수 합이 3이면 순서 관계 없다.
        if digit % 3:
            count = 0
        else:
            count = fac(n)
    elif k == 4:
        # 마지막 자리가 2자리 이상의 4의 배수
        four = 0
        for i in num:
            if i > 10 and i % 4 == 0:
                four += 1
        count = fac(n - 1) * four
        # 마지막 자리가 1자리수
        one = []
        for i in num:
            if i < 10:
                one.append(i)
        merge = 0
        for i in one:
            for j in num:
                if i != j and (j % 10 * 10 + i) % 4 == 0:
                    merge += 1
        count += fac(n - 2) * merge
    elif k == 5:
        five = 0
        for i in num:
            if i % 5 == 0:
                five += 1
        count = fac(n - 1) * fac(five)  # 마지막 자리만 5의 배수이면 나머지는 관계 없다.
    elif k == 6:  # 2의 배수 이면서 3의 배수
        digit = 0
        for i in num:
            for j in str(i):
                digit += int(j)  # 자릿수 합이 3이면 순서 관계 없다.
        if digit % 3:
            count = 0
        else:
            even = 0
            for i in num:
                if i % 2 == 0:
                    even += 1
            count = fac(n - 1) * even  # 마지막 자리만 짝수면 나머지는 관계 없다.
    elif k == 9:
        digit = 0
        for i in num:
            for j in str(i):
                digit += int(j)  # 자릿수 합이 9이면 순서 관계 없다.
        if digit % 9:
            count = 0
        else:
            count = fac(n)
    else:
        count = 0
        permute(num, 0)
    print("#{} {}".format(tc, count))
