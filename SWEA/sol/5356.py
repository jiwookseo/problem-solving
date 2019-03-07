for tc in range(1, int(input())+1):
    s = [input() for _ in range(5)]
    l = [len(i) for i in s]
    ml = max(l)
    temp = ""
    for c in range(ml):
        for r in range(5):
            if l[r] > c:
                temp += s[r][c]
    print("#{} {}".format(tc, temp))
