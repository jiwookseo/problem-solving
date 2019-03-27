# 6193. 준기가 좋아하는 숫자 나열 D6
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPl8P6AHUDFAU4


def remove(l, r):
    rl, rr = "", ""
    for t in range(len(l) - 1, -1, -1):
        if l[t] != r[t]:
            rl += l[t]
            rr += r[t]
    return rl, rr


for TC in range(1, int(input()) + 1):
    N = int(input())
    li = input().replace(" ", "")
    stack = [(*(remove(li[:N], li[N:])), 0)]
    if not stack[0][0]:
        print("#{} 0".format(TC))
        continue
    check = False
    while stack:
        left, right, count = stack.pop(0)
        N = len(left)
        for i in range(N):
            for j in range(N):
                if left[i] != right[j]:
                    tl, tr = remove(left[:i] + right[j] + left[i + 1:], right[:j] + left[i] + right[j + 1:])
                    if not tl:
                        check = True
                        count += 1
                        break
                    stack.append((tl, tr, count + 1))
            if check:
                break
        if check:
            break
    print("#{} {}".format(TC, count))
