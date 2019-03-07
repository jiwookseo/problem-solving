for _ in range(int(input())):
    a, b = [0] * 5, [0] * 5
    for i in map(int, input().split()[1:]):
        a[i] += 1
    for i in map(int, input().split()[1:]):
        b[i] += 1
    check = True
    while len(a) != 1 and check:
        ta, tb = a.pop(), b.pop()
        if ta > tb:
            print('A')
            check = False
        elif ta < tb:
            print('B')
            check = False
    if check:
        print('D')
