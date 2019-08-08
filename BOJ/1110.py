N = num = int(input())
cycle = 0
while True:
    if num < 10:
        num *= 11
    else:
        num = num % 10 * 10 + (num // 10 + num % 10) % 10
    cycle += 1
    if num == N:
        break
print(cycle)
