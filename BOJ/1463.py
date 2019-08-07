x = int(input())
minimum = 10000


def f(num, count=0):
    global minimum
    if count >= minimum:
        return
    if num == 1:
        minimum = count
        return

    count += 1
    if not num % 3:
        f(num // 3, count)
    if not num % 2:
        f(num // 2, count)
    f(num - 1, count)


f(x)
print(minimum)
