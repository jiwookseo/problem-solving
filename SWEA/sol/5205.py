    # 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
    # 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
    def part(a, l, r):
        p = a[l]
        i, j = l, r
        while i <= j:
            while a[i] <= p and i < r:
                i += 1
            while a[j] >= p and j > l:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
            elif i == j:
                break
        a[l], a[j] = a[j], a[l]
        return j


    def qs(a, l, r):
        if l < r:
            m = part(a, l, r)
            qs(a, l, m - 1)
            qs(a, m + 1, r)
        return


    for TC in range(1, int(input()) + 1):
        N = int(input())
        inp = list(map(int, input().split()))
        qs(inp, 0, N - 1)
        result = inp[N // 2]
        print("#{} {}".format(TC, result))