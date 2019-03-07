dwf = [int(input()) for _ in range(9)]
dwf.sort()
for i in range(1 << 9):
    if sum([i & (1 << j) != 0 for j in range(9)]) == 7:
        sub = [dwf[j] for j in range(9) if i & (1 << j)]
        if sum(sub) == 100:
            for k in sub:
                print(k)
            break
