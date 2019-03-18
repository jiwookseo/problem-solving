for TC in range(1, int(input()) + 1):
    r, c = map(int, input().split())
    check = False
    result = []
    for _ in range(r):
        if check:
            input()
        else:
            t = list(input())
            for i in range(c-1, -1, -1):
                if t[i] == '1':
                    result = "".join(t[i-55:i+1])
                    check = True
                    break
    dec = {'0110': 0, '1100': 1, '1001': 2, '1110': 3, '0001': 4, '1000': 5, '0111': 6, '1101': 7, '1011': 8, '0101': 9}
    a = [dec[result[i * 7 + 2:i * 7 + 6]] for i in range(8)]
    odd = sum(a[i] for i in range(0, 7, 2))
    even = sum(a[i] for i in range(1, 7, 2))
    if (odd * 3 + even + a[7]) % 10 == 0:
        print("#{} {}".format(TC, odd + even + a[7]))
    else:
        print("#{} 0".format(TC))
