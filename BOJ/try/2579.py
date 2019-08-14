# recursion / python list stack / python custom stack 시간초과
N = int(input())
stairs = [int(input()) for _ in range(N)]
maximum = 0
stack = [(None, None, None)] * 1000
stack[0] = (0, stairs[0], False)
stack[1] = (1, stairs[1], False)
top = 1
while top != -1:
    floor, count, check = stack[top]
    top -= 1
    if floor == N - 2:
        if not check:
            temp = count + stairs[floor + 1]
            if temp > maximum:
                maximum = temp
    elif floor == N - 3:
        temp = count + stairs[floor + 2]
        if temp > maximum:
            maximum = temp
        if not check:
            top += 1
            stack[top] = (floor + 1, count + stairs[floor + 1], True)
    elif check:
        top += 1
        stack[top] = (floor + 2, count + stairs[floor + 2], False)
    else:
        top += 1
        stack[top] = (floor + 1, count + stairs[floor + 1], True)
        top += 1
        stack[top] = (floor + 2, count + stairs[floor + 2], False)
print(maximum)
