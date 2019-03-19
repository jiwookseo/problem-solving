# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15JEKKAM8CFAYD&categoryId=AV15JEKKAM8CFAYD&categoryType=CODE
dec = {'0110': 0, '1100': 1, '1001': 2, '1110': 3, '0001': 4, '1000': 5, '0111': 6, '1101': 7, '1011': 8, '0101': 9}
for tc in range(1, int(input()) + 1):
    r, c = map(int, input().split())
    code = set()
    prev = None
    inp = []
    for _ in range(r):
        temp = input().strip('0')
        if temp not in inp:
            inp.append(temp)
    for temp in inp:
        for i in code:
            temp = temp.replace(i, "")
        temp = temp.strip('0')
        code.add(temp)
    real = set()
    for cd in code:
        for i in code:
            if i != cd:
                cd = cd.replace(i, "")
        real.add(cd)
    result = 0
    real -= {''}
    for temp in real:
        ans = ''
        for i in temp:
            for j in range(3, -1, -1):
                ans += "1" if int(i, 16) & (1 << j) else "0"
        t = len(ans) - 1
        while ans[t] == "0":
            t -= 1
        ans = '0' * 28 + ans[:t + 1]
        t = 1
        while len(ans) >= t * 56:
            t += 1
        t -= 1
        ans = ans[len(ans) - t * 56:]
        if t > 1:
            ans = "".join([ans[i] for i in range(0, len(ans), t)])
        a = [dec[ans[i * 7 + 2:i * 7 + 6]] for i in range(8)]
        odd = sum(a[i] for i in range(0, 7, 2))
        even = sum(a[i] for i in range(1, 7, 2))
        if (odd * 3 + even + a[7]) % 10 == 0:
            result += odd + even + a[7]
    print("#{} {}".format(tc, result))